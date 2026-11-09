"""Balises SEO qui dépendent du domaine. À relancer à chaque changement de domaine ou de nom :
    python tools/set_domain.py https://www.mon-domaine.fr "Nom du site"
Génère dans chaque page un bloc <!-- SEO:START --> ... <!-- SEO:END --> (canonical, Open Graph, Twitter,
JSON-LD), ainsi que sitemap.xml, robots.txt et llms.txt à la racine du site."""
import io, re, sys, json, datetime, os

S = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
SITE = (sys.argv[1] if len(sys.argv) > 1 else 'https://www.roulelibre.fr').rstrip('/')
NAME = sys.argv[2] if len(sys.argv) > 2 else 'Roulelibre'
TODAY = datetime.date.today().isoformat()
OG = SITE + '/img/og.jpg'

sys.path.insert(0, S + 'tools')
from faq_accueil import FAQ

AUGMENT = {'@type': 'Brand', 'name': 'Augment'}
SELLER = {'@type': 'Organization', 'name': 'Augment Mobility', 'url': 'https://augment.eco/fr-fr/'}

def product(name, desc, img, price, url):
    return {'@type': 'Product', 'name': name, 'description': desc, 'brand': AUGMENT,
            'image': SITE + '/img/' + img,
            'offers': {'@type': 'Offer', 'priceCurrency': 'EUR', 'price': price, 'url': url,
                       'availability': 'https://schema.org/InStock', 'seller': SELLER}}

PRODUCTS = [
    product('Agaru Smart', 'Trottinette électrique pliable, 25 km/h, 50 km d’autonomie, batterie 499 Wh, 20 kg.', 'agaru-profil-deplie.webp', '399', 'https://augment.eco/fr-fr/agaru-smart/'),
    product('Agaru Ultra', 'Trottinette électrique pliable, 25 km/h, 70 km d’autonomie, batterie 768 Wh, 20,7 kg. Location dès 12,95 €/mois.', 'agaru-profil-deplie.webp', '549', 'https://augment.eco/fr-fr/agaru-ultra/'),
    product('E-scooter 360', 'Scooter électrique pliable à assise, 45 km/h, 53 km d’autonomie (106 km avec une seconde batterie), 36 kg. Location dès 25,90 €/mois.', '360-vue-3-4.webp', '1990', 'https://augment.eco/fr-fr/augment-360/'),
]

ORG = {'@type': 'Organization', '@id': SITE + '/#editeur', 'name': NAME, 'legalName': 'Azura', 'url': SITE + '/', 'logo': SITE + '/img/logo-512.png',
       'address': {'@type': 'PostalAddress', 'streetAddress': 'Cours d’Albret', 'addressLocality': 'Bordeaux', 'postalCode': '33000', 'addressCountry': 'FR'},
       'publishingPrinciples': SITE + '/a-propos'}
WEBSITE = {'@type': 'WebSite', '@id': SITE + '/#site', 'name': NAME, 'url': SITE + '/', 'inLanguage': 'fr-FR', 'publisher': {'@id': SITE + '/#editeur'}}

def crumbs(label, path):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': label, 'item': SITE + path}]}

def faq_from_page(html):
    out = []
    for m in re.finditer(r'<summary>.*?class="qa__q">(.*?)</span>.*?</summary>\s*<div class="qa__a">(.*?)</div>\s*</details>', html, re.S):
        q = re.sub(r'<[^>]+>', '', m.group(1)).replace('&nbsp;', ' ').strip()
        a = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(2)).replace('&nbsp;', ' ')).strip()
        if q and a:
            out.append((q, a))
    return out

def faqpage(pairs):
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in pairs]}

PAGES = {
    'index.html': ('/', 'website'),
    'comparateur.html': ('/comparateur', 'article'),
    'configurateur.html': ('/configurateur', 'website'),
    'videos.html': ('/videos', 'website'),
    'a-propos.html': ('/a-propos', 'website'),
    'mentions-legales.html': ('/mentions-legales', 'website'),
    'confidentialite.html': ('/confidentialite', 'website'),
}
LABELS = {'a-propos.html': 'Qui sommes-nous', 'comparateur.html': 'Comparatif', 'configurateur.html': 'Simuler sa location', 'videos.html': 'Vidéos',
          'mentions-legales.html': 'Mentions légales', 'confidentialite.html': 'Confidentialité'}

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;')

sitemap = []
for f, (path, kind) in PAGES.items():
    p = S + f
    html = io.open(p, encoding='utf-8').read()
    html = re.sub(r'\n?<!-- SEO:START -->.*?<!-- SEO:END -->', '', html, flags=re.S)
    title = re.sub(r'<[^>]+>', '', re.search(r'<title>(.*?)</title>', html, re.S).group(1)).replace('&nbsp;', ' ').replace('&amp;', '&')
    desc = re.search(r'<meta name="description" content="([^"]*)"', html).group(1).replace('&nbsp;', ' ').replace('&amp;', '&')
    url = SITE + path
    graph = [ORG, WEBSITE, {'@type': 'AboutPage' if f == 'a-propos.html' else 'WebPage', '@id': url + '#page', 'url': url, 'name': title, 'description': desc,
                            'inLanguage': 'fr-FR', 'isPartOf': {'@id': SITE + '/#site'}, 'dateModified': TODAY}]
    if f == 'index.html':
        graph.append({'@type': 'ItemList', 'name': 'Véhicules électriques Augment vendus en France',
                      'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': pr} for i, pr in enumerate(PRODUCTS)]})
        graph.append(faqpage(FAQ))
    if f == 'comparateur.html':
        graph.append({'@type': 'ItemList', 'name': 'Comparatif Agaru Smart, Agaru Ultra, E-scooter 360',
                      'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'item': pr} for i, pr in enumerate(PRODUCTS)]})
        pairs = faq_from_page(html)
        if pairs:
            graph.append(faqpage(pairs))
    if f in LABELS:
        graph.append(crumbs(LABELS[f], path))
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    block = ('\n<!-- SEO:START -->\n'
             '<link rel="canonical" href="%s">\n'
             '<meta property="og:type" content="%s">\n'
             '<meta property="og:site_name" content="%s">\n'
             '<meta property="og:locale" content="fr_FR">\n'
             '<meta property="og:title" content="%s">\n'
             '<meta property="og:description" content="%s">\n'
             '<meta property="og:url" content="%s">\n'
             '<meta property="og:image" content="%s">\n'
             '<meta property="og:image:width" content="1200">\n'
             '<meta property="og:image:height" content="630">\n'
             '<meta name="twitter:card" content="summary_large_image">\n'
             '<script type="application/ld+json">%s</script>\n'
             '<!-- SEO:END -->') % (url, kind, esc(NAME), esc(title), esc(desc), url, OG, ld)
    html = html.replace('</head>', block + '\n</head>', 1)
    io.open(p, 'w', encoding='utf-8', newline='').write(html)
    if 'noindex' not in html:
        sitemap.append((url, '1.0' if path == '/' else '0.8'))

# Articles de la rubrique Conseils (générés par build_articles.py)
import glob
for _f in sorted(glob.glob(S + 'conseils/*.html')):
    _h = io.open(_f, encoding='utf-8').read()
    _m = re.search(r'<link rel="canonical" href="([^"]+)"', _h)
    if _m and 'noindex' not in _h:
        sitemap.append((_m.group(1), '0.9' if _f.endswith('index.html') else '0.7'))

io.open(S + 'sitemap.xml', 'w', encoding='utf-8', newline='\n').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    ''.join('  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>\n' % (u, TODAY, pr) for u, pr in sitemap) +
    '</urlset>\n')

io.open(S + 'robots.txt', 'w', encoding='utf-8', newline='\n').write(
    '# Moteurs de recherche et moteurs de réponse IA autorisés (citation possible du site).\n'
    'User-agent: *\nAllow: /\nDisallow: /tools/\n\n'
    '# Robot d’entraînement seul (Common Crawl) : non nécessaire.\nUser-agent: CCBot\nDisallow: /\n\n'
    'Sitemap: %s/sitemap.xml\n' % SITE)

io.open(S + 'llms.txt', 'w', encoding='utf-8', newline='\n').write('''# %s

> Site éditorial français consacré aux véhicules électriques Augment vendus en France : trottinettes Agaru Smart et Agaru Ultra, scooter pliable E-scooter 360. Location (abonnement) et achat, prix relevés sur augment.eco. Liens partenaires vers augment.eco (programme d'affiliation AWIN).

## Pages

- [Accueil](%s/) : la gamme, la location expliquée, avis clients, FAQ
- [Comparatif](%s/comparateur) : les 3 modèles critère par critère, guides pratiques, FAQ technique
- [Simulateur de location](%s/configurateur) : prix mensuel selon la durée, l'acompte et les options
- [Vidéos](%s/videos) : tests et avis vidéo

## Prix (France, relevés sur augment.eco)

- Agaru Smart : 399 € à l'achat, ou 19,33 €/mois sur 24 mois (PayPal, TAEG 15,99 %%). Location non proposée en France.
- Agaru Ultra : 549 € à l'achat. Location : 12, 24 ou 36 mois, acompte de 59 à 399 €, de 12,95 à 44,95 €/mois. Réparations comprises dans l'abonnement.
- E-scooter 360 : 1 990 € à l'achat. Location : 12, 24 ou 36 mois, acompte de 290 à 1 490 €, de 25,90 à 159,90 €/mois.
- Retour possible dans les 14 premiers jours de l'abonnement ; option d'achat à tout moment.

Source officielle et prix faisant foi : https://augment.eco/fr-fr/
''' % (NAME, SITE, SITE, SITE, SITE))
print('SEO généré pour', SITE, '—', len(sitemap), 'URL dans le sitemap')
