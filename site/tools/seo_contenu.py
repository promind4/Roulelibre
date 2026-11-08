"""SEO on-page (une seule fois) : titres, descriptions, robots, FAQ de l'accueil.
Les balises qui dépendent du domaine (canonical, Open Graph, JSON-LD, sitemap) sont gérées par set_domain.py."""
import io, re

S = 'D:/AUGMENT ECO/site/'

META = {
    'index.html': ('Location trottinette électrique Augment : Agaru et E-scooter 360',
                   'Louer ou acheter une trottinette électrique Augment : Agaru Smart, Agaru Ultra (70 km) ou scooter pliable E-scooter 360. Abonnement dès 12,95 €/mois, réparations comprises.'),
    'comparateur.html': ('Agaru Smart, Agaru Ultra ou E-scooter 360 : le comparatif',
                         'Comparatif Augment : autonomie, vitesse, poids, batterie, prix à l’achat et en location des Agaru Smart, Agaru Ultra et E-scooter 360, critère par critère.'),
    'configurateur.html': ('Prix location Agaru et E-scooter 360 : simulateur par mois',
                           'Simulez le prix de votre location Augment : durée de 12 à 36 mois, acompte, options vol et casque. Agaru Ultra dès 12,95 €/mois, E-scooter 360 dès 25,90 €/mois.'),
    'videos.html': ('Avis vidéo : tests de l’Agaru et de l’E-scooter 360',
                    'Tests et avis en vidéo de la trottinette Agaru et du scooter électrique pliable E-scooter 360 d’Augment, par des médias et des chaînes spécialisées.'),
    'mentions-legales.html': (None, None),
    'confidentialite.html': (None, None),
}

for f, (title, desc) in META.items():
    p = S + f
    s = io.open(p, encoding='utf-8').read()
    if title:
        s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, s, count=1, flags=re.S)
        s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % desc, s, count=1)
    robots = 'noindex, follow' if f in ('mentions-legales.html', 'confidentialite.html') else 'index, follow, max-image-preview:large, max-snippet:-1'
    if '<meta name="robots"' in s:
        s = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="%s">' % robots, s)
    else:
        s = s.replace('<meta name="theme-color"', '<meta name="robots" content="%s">\n<meta name="theme-color"' % robots, 1)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)

# ---------- FAQ de l'accueil (questions de location, réponses tirées d'augment.eco) ----------
FAQ = [
    ('Peut-on louer une trottinette électrique Augment ?',
     'Oui. En France, l’Agaru Ultra et l’E-scooter 360 se louent en abonnement sur augment.eco : un acompte, puis une mensualité fixe pendant 12, 24 ou 36 mois. L’Agaru Smart est proposée à l’achat (399 €).'),
    ('Combien coûte la location d’une trottinette Augment ?',
     'L’Agaru Ultra se loue dès 12,95 €/mois sur 12 mois avec 399 € d’acompte, ou de 29,95 à 44,95 €/mois avec l’acompte minimal de 59 €. L’E-scooter 360 se loue dès 25,90 €/mois sur 36 mois avec 1 490 € d’acompte.'),
    ('Que comprend l’abonnement ?',
     'Pour l’Agaru Ultra, le service tout compris est inclus : réparations, usure, accidents, batterie, freins et pneus, avec une trottinette de remplacement en cas de panne. Pour l’E-scooter 360, la garantie constructeur est de 2 ans (5 ans sur le cadre) et les pièces d’usure sont disponibles.'),
    ('Peut-on essayer avant de s’engager ?',
     'Oui. Selon la FAQ d’Augment, le véhicule peut être retourné dans les 14 premiers jours de l’abonnement.'),
    ('Peut-on acheter la trottinette à la fin de la location ?',
     'Oui. Augment propose une option d’achat à la fin de l’abonnement, ou à tout moment en payant le solde restant.'),
    ('Quelle différence entre l’Agaru et l’E-scooter 360 ?',
     'L’Agaru est une trottinette électrique pliable limitée à 25 km/h (50 km d’autonomie pour la Smart, 70 km pour l’Ultra). L’E-scooter 360 est un scooter pliable à assise, homologué jusqu’à 45 km/h, avec une batterie amovible et jusqu’à 106 km d’autonomie avec une seconde batterie.'),
]

def faq_html():
    items = ''.join(
        '        <details class="hfaq__item">\n'
        '          <summary><span class="hfaq__q">%s</span><span class="hfaq__icon" aria-hidden="true">+</span></summary>\n'
        '          <p class="hfaq__a">%s</p>\n'
        '        </details>\n' % (q.replace('?', '&nbsp;?').replace(' &nbsp;?', '&nbsp;?'), a) for q, a in FAQ)
    return ('  <!-- ============================== FAQ ==============================\n'
            '       Réponses tirées d’augment.eco (FAQ, tunnel de commande, page Notre histoire). Reprises en JSON-LD (FAQPage) par set_domain.py. -->\n'
            '  <section class="section hfaq" id="faq" aria-labelledby="faq-title">\n'
            '    <div class="wrap hfaq__grid">\n'
            '      <div class="hfaq__head">\n'
            '        <p class="eyebrow">Questions fréquentes</p>\n'
            '        <h2 id="faq-title">Louer une trottinette Augment&nbsp;: l’essentiel.</h2>\n'
            '      </div>\n'
            '      <div class="hfaq__list">\n' + items +
            '      </div>\n'
            '    </div>\n'
            '  </section>\n\n')

p = S + 'index.html'
s = io.open(p, encoding='utf-8').read()
if 'id="faq"' not in s:
    a = '  <!-- ============================== SOUSCRIRE ============================== -->'
    assert a in s
    s = s.replace(a, faq_html() + a)
io.open(p, 'w', encoding='utf-8', newline='').write(s)

c = io.open(S + 'css/home.css', encoding='utf-8').read()
if '.hfaq' not in c:
    c = c.rstrip('\n') + '''

/* ---------- FAQ de l'accueil ---------- */
.hfaq__grid { display: grid; grid-template-columns: minmax(0, .8fr) minmax(0, 1.2fr); gap: clamp(28px, 5vw, 80px); align-items: start; }
.hfaq__head { display: flex; flex-direction: column; gap: 18px; position: sticky; top: 110px; }
.hfaq__list { display: grid; gap: 10px; }
.hfaq__item { background: var(--white); border: 1px solid var(--line-soft); border-radius: var(--radius); }
.hfaq__item summary { list-style: none; cursor: pointer; display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 18px 20px; font-weight: 600; font-size: 16.5px; }
.hfaq__item summary::-webkit-details-marker { display: none; }
.hfaq__icon { font-family: var(--f-mono); font-size: 20px; color: var(--accent); transition: transform .2s var(--ease); flex: none; }
.hfaq__item[open] .hfaq__icon { transform: rotate(45deg); }
.hfaq__a { margin: 0; padding: 0 20px 18px; color: var(--muted); font-size: 15.5px; line-height: 1.6; max-width: 70ch; }
@media (max-width: 860px) { .hfaq__grid { grid-template-columns: 1fr; } .hfaq__head { position: static; } }
'''
    io.open(S + 'css/home.css', 'w', encoding='utf-8', newline='').write(c)

io.open(S + 'tools/faq_accueil.py', 'w', encoding='utf-8').write('FAQ = ' + repr(FAQ) + '\n')
print('ok')
