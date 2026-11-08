"""Tracker de prix : relève les prix officiels d'augment.eco (même requête publique que leur site), les compare
à ce qu'affiche Roulelibre et signale (ou applique) les écarts.

    python tools/tracker_prix.py              # relevé + rapport (ne modifie pas le site)
    python tools/tracker_prix.py --appliquer  # corrige aussi les prix sans ambiguïté dans les pages

Sortie : tools/data/releve_AAAA-MM-JJ.json (historique), tools/data/etat_site.json (ce que le site affiche),
tools/data/rapport.md (écarts). Code de sortie : 0 = rien à signaler, 1 = écart détecté, 2 = erreur de relevé.
Une seule requête par exécution et par mode (2 au total) : lancer au plus une fois par jour."""
import io, os, re, sys, json, glob, datetime, urllib.request
if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
DATA = ROOT + 'tools/data/'
os.makedirs(DATA, exist_ok=True)
API = 'https://api.augment.eco/graphql-public'
QUERY = io.open(DATA + 'requete.graphql', encoding='utf-8').read()
APPLY = '--appliquer' in sys.argv
TODAY = datetime.date.today().isoformat()

def call(mode):
    body = json.dumps({'operationName': 'configurableItems',
                       'variables': {'country': 'FR', 'language': 'FR', 'checkoutMode': mode}, 'query': QUERY}).encode()
    req = urllib.request.Request(API, body, {'content-type': 'application/json', 'apollographql-client-name': 'roulelibre-tracker'})
    return json.load(urllib.request.urlopen(req, timeout=30))['data']['saleableItems']

def A(v):
    return [] if v is None else (v if isinstance(v, list) else [v])

def normalise(items_buy, items_sub):
    out = {}
    subs = {x['name']: x for x in items_sub}
    for x in items_buy:
        s = subs.get(x['name'], x)
        fin = A(x.get('financingInfo'))
        out[x['name']] = {
            'achat': x['purchaseAmountInCents'],
            'options': sorted(x['checkoutOptions']),
            'stock': (x.get('availability') or {}).get('code'),
            'livraison': x.get('shippingTimeInBusinessDays'),
            'financement': {'mois': fin[0]['durationInMonths'], 'mensualite': fin[0]['installmentAmountInCents'],
                            'total': fin[0]['totalAmountPayableInCents'], 'taeg': fin[0]['annualPercentageRate']} if fin else None,
            'grille': {str(d['durationInMonths']): {str(p['amountInCents']): p['monthlyAmountInCents'] for p in d['downPayments']}
                       for d in A((x.get('planDetails') or {}).get('durations'))} if 'SUBSCRIPTION' in x['checkoutOptions'] else None,
            'services': {sv['id']: sv['extraMonthlyAmountInCents'] for sv in A(s.get('services'))},
            'accessoires': {o['id']: [o['amountInCents'], o['extraMonthlyAmountInCents']] for a in A(x.get('accessories')) for o in A(a.get('options'))},
        }
    return out

def fr(cents, nb='&nbsp;'):
    """12345 -> '123,45' ; entier si pas de centimes (399 -> '399'); milliers séparés (nb)."""
    e, c = divmod(cents, 100)
    s = '{:,}'.format(e).replace(',', nb)
    return s + (',%02d' % c if c else '')

try:
    nouveau = normalise(call('PURCHASE'), call('SUBSCRIPTION'))
except Exception as e:
    print('ERREUR de relevé :', e)
    sys.exit(2)
io.open(DATA + 'releve_%s.json' % TODAY, 'w', encoding='utf-8').write(json.dumps(nouveau, indent=1, ensure_ascii=False))
io.open(DATA + 'releve_dernier.json', 'w', encoding='utf-8').write(json.dumps(nouveau, indent=1, ensure_ascii=False))

etat_p = DATA + 'etat_site.json'
if not os.path.exists(etat_p):
    sys.exit('etat_site.json absent : créer la référence de ce que le site affiche.')
etat = json.load(io.open(etat_p, encoding='utf-8'))

ecarts, applicables = [], []
def cmp(chemin, ancien, neuf):
    if ancien != neuf:
        ecarts.append((chemin, json.loads(json.dumps(ancien)), json.loads(json.dumps(neuf))))

for nom, n in nouveau.items():
    e = etat.get(nom)
    if e is None:
        ecarts.append((nom, 'absent du site', 'NOUVEAU MODÈLE chez Augment'))
        continue
    for k in ('achat', 'options', 'stock', 'financement', 'grille', 'services', 'accessoires'):
        cmp('%s.%s' % (nom, k), e.get(k), n.get(k))
for nom in etat:
    if nom not in nouveau:
        ecarts.append((nom, 'affiché sur le site', 'MODÈLE RETIRÉ de la vente'))

# ---- application automatique (valeurs sans ambiguïté seulement) ----
toutes = []
for nom, e in etat.items():
    toutes += [e['achat']]
    if e.get('financement'):
        toutes += [e['financement']['mensualite'], e['financement']['total']]
    for g in (e.get('grille') or {}).values():
        toutes += [int(k) for k in g] + list(g.values())
    toutes += list(e.get('services', {}).values()) + [v for a in e.get('accessoires', {}).values() for v in a]

def remplacer(ancien_c, nouveau_c, libelle, formes):
    """formes : liste de (motif_ancien, motif_nouveau) ; applique à toutes les pages si la valeur est unique."""
    if toutes.count(ancien_c) > 1:
        return False, 'ambigu (même montant utilisé ailleurs) : à corriger avec l’assistant'
    n = 0
    # pages, articles, scripts du site, et générateurs qui réécrivent ces pages (sinon l'ancien prix reviendrait)
    fichiers = (glob.glob(ROOT + '*.html') + glob.glob(ROOT + 'conseils/*.html') + glob.glob(ROOT + 'js/*.js') + [ROOT + 'llms.txt'] +
                [ROOT + 'tools/' + g for g in ('set_domain.py', 'articles_contenu.py', 'faq_accueil.py', 'seo_motscles.py', 'seo_contenu.py', 'page_apropos.py')])
    fichiers = [f for f in fichiers if os.path.exists(f)]
    for f in fichiers:
        t = io.open(f, encoding='utf-8').read(); o = t
        for a, b in formes:
            t = re.sub(r'(?<![\d,.])' + re.escape(a) + r'(?![\d])', b, t)
        if t != o:
            n += 1
            if APPLY:
                io.open(f, 'w', encoding='utf-8', newline='').write(t)
    return True, '%d fichier(s)' % n

notes = []
for nom, n in nouveau.items():
    e = etat.get(nom)
    if not e:
        continue
    if n['achat'] != e['achat']:
        a, b = e['achat'], n['achat']
        formes = [(fr(a), fr(b)), (fr(a, ' '), fr(b, ' ')), (fr(a, ''), fr(b, ''))]
        ok, msg = remplacer(a, b, 'prix achat ' + nom, formes)
        notes.append('Prix d’achat %s : %s → %s € : %s' % (nom, fr(a, ' '), fr(b, ' '), msg))
        if ok: e['achat'] = b
    if e.get('financement') and n.get('financement') and e['financement'] != n['financement']:
        for cle, lib in (('mensualite', 'mensualité de financement'), ('total', 'montant total dû')):
            a, b = e['financement'][cle], n['financement'][cle]
            if a != b:
                formes = [(fr(a), fr(b)), (fr(a, ' '), fr(b, ' ')), (fr(a, '').replace(',', '.'), fr(b, '').replace(',', '.'))]
                ok, msg = remplacer(a, b, lib + ' ' + nom, formes)
                notes.append('%s %s : %s → %s € : %s' % (lib.capitalize(), nom, fr(a, ' '), fr(b, ' '), msg))
                if ok: e['financement'][cle] = b
        e['financement']['taeg'] = n['financement']['taeg']; e['financement']['mois'] = n['financement']['mois']

if APPLY:
    io.open(etat_p, 'w', encoding='utf-8').write(json.dumps(etat, indent=1, ensure_ascii=False))

rest = [c for c in ecarts if not (c[0].endswith('.achat') or c[0].endswith('.financement'))]
with io.open(DATA + 'rapport.md', 'w', encoding='utf-8') as r:
    r.write('# Rapport du tracker, %s\n\n' % TODAY)
    if not ecarts:
        r.write('Aucun écart : le site affiche les prix actuels d’augment.eco.\n')
    else:
        r.write('## Écarts entre augment.eco et le site\n\n')
        for c, a, b in ecarts:
            r.write('- `%s` : site = %s, augment.eco = %s\n' % (c, json.dumps(a, ensure_ascii=False), json.dumps(b, ensure_ascii=False)))
        r.write('\n## Actions\n\n')
        for nt in notes:
            r.write('- %s%s\n' % (nt, ' (appliqué)' if APPLY and 'ambigu' not in nt else ''))
        if rest:
            r.write('- Autres écarts (grille, options, stock, nouveau modèle) : à traiter avec l’assistant.\n')
print(io.open(DATA + 'rapport.md', encoding='utf-8').read())
sys.exit(1 if ecarts else 0)
