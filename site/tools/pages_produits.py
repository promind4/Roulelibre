# -*- coding: utf-8 -*-
"""Pages produits (une par véhicule) : avis, prix, location, fiche technique, FAQ.
    python tools/pages_produits.py      ->  agaru-ultra.html (puis lancer tools/set_domain.py)
Gabarit : en-tête et pied de page de mentions-legales.html, mise en forme des articles (css/article.css).
Les prix viennent du relevé augment.eco (tools/data/releve_dernier.json, mis à jour par tools/tracker_prix.py).
Règles : aucune expérience inventée, chiffres de la fiche constructeur ou du tunnel de commande, sources citées."""
import io, os, re, json, html as H

S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace(chr(92), '/') + '/'
R = json.load(io.open(S + 'tools/data/releve_dernier.json', encoding='utf-8'))
AWIN = 'https://www.awin1.com/cread.php?awinmid=131358&amp;awinaffid=3099440&amp;ued={}&amp;platform=pl'


def eur(cents, dec=True):
    v = cents / 100.0
    s = ('%.2f' % v).replace('.', ',') if dec and v != int(v) else '%d' % v
    if len(s.split(',')[0]) > 3:
        a, *b = s.split(',')
        s = a[:-3] + '&nbsp;' + a[-3:] + (',' + b[0] if b else '')
    return s + '&nbsp;€'


def grille_html(g, nom):
    acs = sorted(int(a) for a in next(iter(g.values())))
    rows = ''.join('<tr><th scope="row">%s mois</th>%s</tr>' % (d, ''.join('<td>%s</td>' % eur(g[d][str(a)]) for a in acs)) for d in sorted(g, key=int))
    return ('<div class="art-table-wrap"><table class="art-table"><caption>Abonnement %s : mensualité selon la durée et l’acompte (relevé augment.eco)</caption>'
            '<thead><tr><th scope="col">Durée</th>%s</tr></thead><tbody>%s</tbody></table></div>') % (
        nom, ''.join('<th scope="col">Acompte %s</th>' % eur(a) for a in acs), rows)


def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;')


# ---------------------------------------------------------------------------------------------------- Agaru Ultra
u = R['agaru-ultra']
g = u['grille']
mini = min(v for d in g.values() for v in d.values())
maxi = max(v for d in g.values() for v in d.values())
f = u['financement']
cout36 = 5900 + 36 * g['36']['5900']

ULTRA = dict(
    fichier='agaru-ultra.html',
    nom='Agaru Ultra',
    titre='Agaru Ultra : avis, prix, location et fiche technique',
    description='Agaru Ultra d’Augment : 70 km d’autonomie, 768 Wh, 20,7 kg. %s à l’achat ou location dès %s/mois, réparations comprises. Avis et fiche technique.'
                % (eur(u['achat']).replace('&nbsp;', ' '), eur(mini).replace('&nbsp;', ' ')),
    eyebrow='Trottinette électrique · Augment',
    h1='Agaru Ultra&nbsp;: notre avis, son prix et la location',
    chapo='La trottinette la plus endurante de la gamme Augment&nbsp;: 70&nbsp;km annoncés, une batterie de 768&nbsp;Wh et un service de réparation compris en location. Ce qu’elle vaut, ce qu’elle coûte et à qui elle convient.',
    hero=('agaru-studio-3-4-avant', 1536, 1024, 'Trottinette électrique Augment Agaru Ultra vue de trois quarts avant, potence noire marquée augment'),
    bref=[
        'Trottinette électrique pliable limitée à 25&nbsp;km/h&nbsp;: 70&nbsp;km d’autonomie annoncée, 50 à 60&nbsp;km au quotidien, 20,7&nbsp;kg.',
        '%s à l’achat, ou en abonnement de %s à %s par mois selon la durée et l’acompte, réparations comprises.' % (eur(u['achat']), eur(mini), eur(maxi)),
        'Même cadre que l’Agaru Smart&nbsp;: la différence tient à la batterie (768&nbsp;Wh contre 499&nbsp;Wh) et à la location, ouverte seulement pour l’Ultra.',
        'Nous ne l’avons pas encore essayée sur la durée&nbsp;: cet avis s’appuie sur la fiche technique, les essais vidéo et les avis clients publics.',
    ],
    corps='''
<h2 id="avis">Notre avis sur l’Agaru Ultra</h2>
<p>L’Agaru Ultra vise les trajets quotidiens de 10 à 25&nbsp;km aller-retour, sans recharger tous les soirs. Sa vraie différence n’est pas technique&nbsp;: c’est la formule d’abonnement, qui inclut les réparations et le remplacement des pièces.</p>
<h3>Les points forts</h3>
<ul class="check">
 <li><strong>L’autonomie</strong>&nbsp;: 768&nbsp;Wh, soit 70&nbsp;km annoncés et 50 à 60&nbsp;km en usage réel, de quoi tenir plusieurs jours de trajets.</li>
 <li><strong>Le service en location</strong>&nbsp;: réparations et remplacements compris pendant toute la durée de l’abonnement, batterie incluse.</li>
 <li><strong>L’équipement</strong>&nbsp;: écran LED, clignotants intégrés aux poignées (option gratuite), verrouillage et statistiques dans l’application.</li>
 <li><strong>Étanche IPX5</strong>&nbsp;: elle supporte la pluie et les projections d’eau.</li>
 <li><strong>Les conditions</strong>&nbsp;: livraison en 3 à 4 jours ouvrés pour les modèles en stock et 14&nbsp;jours pour changer d’avis, selon Augment.</li>
</ul>
<h3>Les points faibles</h3>
<ul class="dash">
 <li><strong>20,7&nbsp;kg</strong>&nbsp;: elle se plie vite, mais se porte difficilement sur plusieurs étages.</li>
 <li><strong>Le freinage</strong>&nbsp;: un disque mécanique à l’arrière et un frein électronique à l’avant, sans freins hydrauliques.</li>
 <li><strong>Le coût total en location</strong>&nbsp;: sur 36&nbsp;mois avec le plus petit acompte, vous payez environ %(cout36)s, contre %(achat)s à l’achat comptant. Vous payez le service et la tranquillité.</li>
</ul>
<p><strong>Pour qui&nbsp;?</strong> Les salariés qui roulent tous les jours et ne veulent pas gérer l’entretien. <strong>Pas pour</strong> ceux qui roulent peu ou qui doivent monter leur trottinette chez eux tous les jours&nbsp;: l’<a href="/conseils/agaru-smart-ou-agaru-ultra-difference">Agaru Smart</a> suffit alors, pour 150&nbsp;€ de moins à l’achat.</p>

<h2 id="fiche-technique">Fiche technique de l’Agaru Ultra</h2>
<div class="art-table-wrap">
<table class="art-table art-table--fiche">
 <caption>Caractéristiques de l’Agaru Ultra (fiche constructeur)</caption>
 <tbody>
  <tr><th scope="row">Catégorie</th><td>Trottinette électrique (EDPM)</td></tr>
  <tr><th scope="row">Vitesse maximale</th><td>25&nbsp;km/h</td></tr>
  <tr><th scope="row">Autonomie</th><td>Jusqu’à 70&nbsp;km (50 à 60&nbsp;km au quotidien)</td></tr>
  <tr><th scope="row">Batterie</th><td>768&nbsp;Wh, fixe, intégrée au plateau</td></tr>
  <tr><th scope="row">Temps de charge</th><td>Environ 7&nbsp;h&nbsp;30 (0 à 100&nbsp;%%)</td></tr>
  <tr><th scope="row">Moteur</th><td>500&nbsp;W (800&nbsp;W en crête), couple 26&nbsp;Nm</td></tr>
  <tr><th scope="row">Pente maximale</th><td>23&nbsp;%%</td></tr>
  <tr><th scope="row">Poids</th><td>20,7&nbsp;kg</td></tr>
  <tr><th scope="row">Pneus</th><td>10 × 2,5 pouces, à air</td></tr>
  <tr><th scope="row">Freinage</th><td>Disque mécanique à l’arrière, frein électronique (eABS) à l’avant</td></tr>
  <tr><th scope="row">Étanchéité</th><td>IPX5</td></tr>
  <tr><th scope="row">Équipements</th><td>Écran LED, clignotants intégrés (option gratuite), application mobile avec antivol digital</td></tr>
 </tbody>
</table>
</div>
<figure class="pgal">
 <img src="/img/agaru-profil-plie-800.webp" width="800" height="330" alt="Agaru Ultra pliée, vue de profil" loading="lazy">
 <img src="/img/agaru-cockpit-800.webp" width="800" height="526" alt="Guidon de l’Agaru Ultra avec son écran LED" loading="lazy">
 <img src="/img/agaru-plateau-frein-800.webp" width="800" height="728" alt="Plateau et frein à disque arrière de l’Agaru Ultra" loading="lazy">
 <img src="/img/agaru-studio-3-4-arriere-800.webp" width="800" height="533" alt="Agaru Ultra vue de trois quarts arrière" loading="lazy">
</figure>

<h2 id="prix">Prix de l’Agaru Ultra&nbsp;: achat, financement ou abonnement</h2>
<ul class="check">
 <li><strong>Achat comptant</strong>&nbsp;: %(achat)s.</li>
 <li><strong>Paiement en plusieurs fois</strong>&nbsp;: %(fin_m)s par mois pendant %(fin_n)s&nbsp;mois, crédit PayPal au TAEG fixe de %(taeg)s, soit %(fin_t)s au total. Un crédit vous engage et doit être remboursé.</li>
 <li><strong>Abonnement</strong>&nbsp;: de %(mini)s à %(maxi)s par mois, réparations comprises, avec une option d’achat en fin de contrat.</li>
</ul>
%(grille)s
<p>Plus l’acompte est élevé, plus la mensualité baisse. La couverture contre le vol s’ajoute pour 2,95&nbsp;€ par mois. Pour comparer les formules avec vos propres réglages, utilisez le <a href="/configurateur">simulateur de location</a>.</p>

<h2 id="louer-ou-acheter">Louer ou acheter l’Agaru Ultra&nbsp;?</h2>
<p><strong>La location</strong> convient si vous voulez un budget mensuel fixe, sans frais de réparation imprévus, et la possibilité de changer de modèle plus tard. <strong>L’achat</strong> revient nettement moins cher si vous gardez la trottinette plusieurs années et que vous savez faire l’entretien courant. Nous détaillons le calcul dans <a href="/conseils/louer-ou-acheter-trottinette-electrique">louer ou acheter une trottinette électrique</a>.</p>
<p>Bon à savoir&nbsp;: l’abonnement peut être pris en charge en partie par votre employeur grâce au <a href="/conseils/forfait-mobilites-durables-trottinette-electrique">forfait mobilités durables</a>.</p>

<h2 id="avis-clients">Ce qu’en disent les clients et les essais</h2>
<p>Sur Trustpilot, Augment obtient 4,0 sur 5 sur 5&nbsp;279&nbsp;avis, tous modèles et tous pays confondus. Les clients citent surtout le rapport qualité-prix, la maintenance comprise, la rapidité de livraison, la facilité de pliage et la qualité de l’application et du support.</p>
<p>Côté essais, le journal La Provence a testé la trottinette d’Augment en conditions réelles. Retrouvez cet essai et les autres sur notre page <a href="/videos">tests en vidéo</a>.</p>

<h2 id="alternatives">Agaru Ultra, Agaru Smart ou E-scooter 360&nbsp;?</h2>
<p>L’<strong>Agaru Smart</strong> a le même cadre avec une batterie plus petite (499&nbsp;Wh, 50&nbsp;km annoncés) pour %(smart)s, mais elle ne se loue pas en France. L’<strong>E-scooter 360</strong> est un scooter pliable à assise qui roule à 45&nbsp;km/h&nbsp;: il demande un permis, une carte grise et une assurance de cyclomoteur. Tous les écarts sont dans notre <a href="/comparateur">comparatif des trois modèles</a>.</p>
''' % dict(cout36=eur(cout36), achat=eur(u['achat']), fin_m=eur(f['mensualite']), fin_n=f['mois'], taeg=('%.2f' % (f['taeg'] * 100)).replace('.', ',') + '&nbsp;%',
           fin_t=eur(f['total']), mini=eur(mini), maxi=eur(maxi), grille=grille_html(g, 'Agaru Ultra'), smart=eur(R['agaru-smart']['achat'])),
    cta_t='Prête à rouler en Agaru Ultra&nbsp;?',
    cta_x='Simulez votre mensualité, puis finalisez votre commande sur le site d’Augment.',
    cta_b=['<a class="btn btn--primary" href="/configurateur?model=ultra">Simuler ma location <span class="arr" aria-hidden="true">→</span></a>',
           '<a class="btn btn--ink" href="%s" target="_blank" rel="sponsored noopener" title="Lien partenaire">Voir l’Agaru Ultra sur augment.eco <span class="arr" aria-hidden="true">→</span></a>'
           % AWIN.format('https%3A%2F%2Faugment.eco%2Ffr-fr%2Fagaru-ultra%2F')],
    faq=[
        ('Quelle est l’autonomie réelle de l’Agaru Ultra ?', 'Augment annonce jusqu’à 70 km. Au quotidien, comptez 50 à 60 km selon votre poids, le relief, le mode de vitesse et la température : le froid peut retirer 20 à 30 % d’autonomie.'),
        ('Combien coûte la location de l’Agaru Ultra ?', 'De %s à %s par mois selon la durée (12, 24 ou 36 mois) et l’acompte choisi, réparations comprises. La couverture contre le vol s’ajoute pour 2,95 € par mois.' % (H.unescape(eur(mini)), H.unescape(eur(maxi)))),
        ('Combien pèse l’Agaru Ultra ?', '20,7 kg. Elle se plie rapidement pour le train ou le bureau, mais reste lourde à porter dans les escaliers.'),
        ('L’Agaru Ultra est-elle étanche ?', 'Elle est certifiée IPX5 : elle résiste à la pluie et aux projections d’eau, mais ne doit pas être immergée ni passée au jet haute pression.'),
        ('Peut-on acheter l’Agaru Ultra à la fin de la location ?', 'Oui. Augment propose une option d’achat à la fin de l’abonnement, ou à tout moment en réglant le solde restant.'),
        ('Faut-il une assurance pour rouler en Agaru Ultra ?', 'Oui. Comme toute trottinette électrique, elle doit être couverte par une assurance responsabilité civile. La couverture vol d’Augment ne remplace pas cette assurance.'),
    ],
    sources=[
        ('https://augment.eco/fr-fr/agaru-ultra/', 'Fiche Agaru Ultra et tunnel de commande, augment.eco (prix relevés le %s)' % '15/11/2026'),
        ('https://www.trustpilot.com/review/augment.eco', 'Avis clients Augment, Trustpilot'),
        ('https://www.service-public.fr/particuliers/vosdroits/F308', 'Engins de déplacement personnel motorisés, service-public.fr'),
    ],
)


# ---------------------------------------------------------------------------------------------------- gabarit
def page(p):
    src = io.open(S + 'mentions-legales.html', encoding='utf-8').read()
    head, rest = src.split('<main id="contenu">', 1)
    foot = rest.split('</main>', 1)[1]
    head = head.replace('css/legal.css', 'css/article.css').replace(' aria-current="page"', '')
    head = re.sub(r'<title>.*?</title>', '<title>%s</title>' % p['titre'], head, count=1, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % esc(p['description']), head, count=1)
    head = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">', head, count=1)
    head = re.sub(r'\n?<!-- SEO:START -->.*?<!-- SEO:END -->', '', head, flags=re.S)
    toc = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', p['corps'])
    img, w, h, alt = p['hero']
    faq = ''.join('<details class="hfaq__item"><summary><span class="hfaq__q">%s</span><span class="hfaq__icon" aria-hidden="true">+</span></summary><p class="hfaq__a">%s</p></details>'
                  % (q.replace(' ?', '&nbsp;?'), a) for q, a in p['faq'])
    import datetime
    mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    d = datetime.date.today()
    maj = '%d %s %d' % (d.day, mois[d.month - 1], d.year)
    main = '''<main id="contenu">
  <article class="art art--produit">
    <header class="wrap art__head">
      <nav class="art__crumbs" aria-label="Fil d’Ariane"><a href="/">Accueil</a><span aria-hidden="true">/</span><a href="/comparateur">Comparatif</a><span aria-hidden="true">/</span><span>%(nom)s</span></nav>
      <p class="eyebrow">%(eyebrow)s</p>
      <h1>%(h1)s</h1>
      <p class="lead art__chapo">%(chapo)s</p>
      <p class="art__meta"><span>Par <a href="/a-propos">la rédaction de Roulelibre</a></span><span>Relu par <a href="/a-propos#qui">l’éditeur</a></span><span>Prix vérifiés le %(maj)s</span></p>
    </header>
    <figure class="wrap art__hero art__hero--produit">
      <img src="/img/%(img)s.webp" srcset="/img/%(img)s-800.webp 800w, /img/%(img)s.webp %(w)dw" sizes="(max-width: 1100px) 100vw, 1100px" width="%(w)d" height="%(h)d" alt="%(alt)s" fetchpriority="high">
    </figure>
    <div class="wrap art__layout">
      <aside class="art__toc" aria-label="Sommaire"><p class="label">Au sommaire</p>%(toc)s</aside>
      <div class="art__body">
        <div class="art__brief"><p class="art__brief-t">En bref</p><ul>%(bref)s</ul></div>
%(corps)s
        <section class="art__cta" aria-label="Passer à l’action">
          <p class="art__cta-t">%(cta_t)s</p>
          <p>%(cta_x)s</p>
          <div class="art__cta-btns">%(cta_b)s</div>
          <p class="art__cta-note">Le bouton vers augment.eco est un lien partenaire&nbsp;: <a href="/a-propos#financement">comment le site est financé</a>.</p>
        </section>
        <section class="art__faq" aria-labelledby="faq-art"><h2 id="faq-art">Questions fréquentes</h2>%(faq)s</section>
        <section class="art__sources" aria-labelledby="src-art"><h2 id="src-art" class="label">Sources</h2><ul>%(sources)s</ul><p>En cas d’écart, le prix affiché sur augment.eco au moment de la commande fait foi. <a href="/a-propos#methode">Notre méthode</a>.</p></section>
      </div>
    </div>
  </article>
</main>''' % dict(p, maj=maj, img=img, w=w, h=h, alt=esc(alt), toc=''.join('<a href="#%s">%s</a>' % (i, re.sub('<[^>]+>', '', t)) for i, t in toc),
                  bref=''.join('<li>%s</li>' % b for b in p['bref']), cta_b=''.join(p['cta_b']), faq=faq,
                  sources=''.join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % s for s in p['sources']))
    io.open(S + p['fichier'], 'w', encoding='utf-8', newline='').write(head + main + foot)
    print(p['fichier'], 'ok')


if __name__ == '__main__':
    page(ULTRA)
