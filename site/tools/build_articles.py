# -*- coding: utf-8 -*-
"""Génère la rubrique Conseils : conseils/index.html + une page par article (tools/articles_contenu.py).
    python tools/build_articles.py [https://www.roulelibre.fr] [Roulelibre]
Gabarit (en-tête, pied de page, cookies) repris de a-propos.html, liens internes absolus (voir absolutise)."""
import io, re, os, sys, json, datetime, hashlib, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
sys.path.insert(0, ROOT + 'tools')
from articles_contenu import ARTICLES

SITE = (sys.argv[1] if len(sys.argv) > 1 else 'https://www.roulelibre.fr').rstrip('/')
NAME = sys.argv[2] if len(sys.argv) > 2 else 'Roulelibre'
MAJ = datetime.date.today().isoformat()
MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
def date_fr(iso):
    y, m, d = iso.split('-'); return '%d %s %s' % (int(d), MOIS[int(m) - 1], y)

src = io.open(ROOT + 'a-propos.html', encoding='utf-8').read()
src = re.sub(r'\n?<!-- SEO:START -->.*?<!-- SEO:END -->', '', src, flags=re.S)
head, rest = src.split('<main id="contenu">', 1)
foot = rest.split('</main>', 1)[1]
head = head.replace('css/legal.css', 'css/article.css')
head = head.replace(' aria-current="page"', '').replace('<a href="conseils/index.html"><small>05</small>', '<a href="conseils/index.html" aria-current="page"><small>05</small>')

import posixpath

def _propre(path):
    """Chemin absolu sans .html (Vercel sert les URL propres, cleanUrls) : /x/index -> /x, /index -> /."""
    if path.endswith('.html'):
        path = path[:-5]
    if path == '/index':
        return '/'
    if path.endswith('/index'):
        return path[:-6] or '/'
    return path

def _resoudre(val, base):
    if re.match(r'(https?:|#|mailto:|data:|//|tel:|javascript:)', val) or val == '':
        return val
    m = re.match(r'([^?#]*)(.*)', val, re.S)
    path, tail = m.group(1), m.group(2)
    if path == '':
        return val
    if not path.startswith('/'):
        path = posixpath.normpath(posixpath.join(base, path))
    return _propre(path) + tail

def absolutise(html, base):
    """Réécrit les liens relatifs en liens absolus depuis la racine du site. Une page servie sans barre finale
    (/conseils) résout les liens relatifs depuis / et non depuis /conseils/ : les liens absolus évitent ce piège."""
    def fix(m):
        attr, val = m.group(1), m.group(2)
        if attr == 'srcset':
            parts = []
            for p in val.split(','):
                bits = p.strip().split(' ', 1)
                bits[0] = _resoudre(bits[0], base)
                parts.append(' '.join(bits))
            return '%s="%s"' % (attr, ', '.join(parts))
        return '%s="%s"' % (attr, _resoudre(val, base))
    return re.sub(r'\b(href|src|srcset)="([^"]*)"', fix, html)

head, foot = absolutise(head, '/'), absolutise(foot, '/')
BY = {a['slug']: a for a in ARTICLES}

# Dates honnêtes : « Mis à jour le » ne change que si le contenu visible de l'article change
# (titre, chapô, corps, FAQ, sources, image), pas à chaque génération. Mémoire : tools/data/dates_articles.json.
DATES_F = ROOT + 'tools/data/dates_articles.json'
try:
    D = json.load(io.open(DATES_F, encoding='utf-8'))
except (OSError, ValueError):
    D = {}

def _empreinte(a):
    vis = {k: a.get(k) for k in ('h1', 'chapo', 'en_bref', 'corps', 'faq', 'sources', 'image', 'cta')}
    return hashlib.sha1(json.dumps(vis, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()

def _date_git(slug):
    """Date du premier commit de la page (date de publication réelle), sinon None."""
    try:
        out = subprocess.run(['git', 'log', '--diff-filter=A', '--format=%as', '--', 'conseils/%s.html' % slug],
                             cwd=ROOT, capture_output=True, text=True, timeout=20).stdout.split()
        return out[-1] if out else None
    except (OSError, subprocess.SubprocessError):
        return None

for _a in ARTICLES:
    _h, _e = _empreinte(_a), D.get(_a['slug'])
    if _e is None:
        _d0 = _date_git(_a['slug']) or MAJ
        D[_a['slug']] = {'publie': _d0, 'maj': _d0, 'empreinte': _h}
    elif _e['empreinte'] != _h:
        _e['maj'], _e['empreinte'] = MAJ, _h

def esc(s): return s.replace('&', '&amp;').replace('"', '&quot;')
def txt(h): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h).replace('&nbsp;', ' ').replace('&amp;', '&')).strip()

def seo_block(url, title, desc, image, kind, ld):
    return ('\n<!-- SEO:START -->\n<link rel="canonical" href="%s">\n<meta property="og:type" content="%s">\n<meta property="og:site_name" content="%s">\n'
            '<meta property="og:locale" content="fr_FR">\n<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n'
            '<meta property="og:url" content="%s">\n<meta property="og:image" content="%s">\n<meta name="twitter:card" content="summary_large_image">\n'
            '<script type="application/ld+json">%s</script>\n<!-- SEO:END -->\n') % (url, kind, esc(NAME), esc(title), esc(desc), url, image,
            json.dumps(ld, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))

def page_head(title, desc, block):
    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, head, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % esc(desc), h, count=1)
    return h.replace('</head>', block + '</head>', 1)

ORG = {'@type': 'Organization', '@id': SITE + '/#editeur', 'name': NAME, 'url': SITE + '/'}

def vignette(a):
    img = a['image'][0]
    return '%s.svg' % img if a.get('anim') else '%s-800.webp' % img

def carte(a, small=False):
    img, alt = a['image']
    return ('<li class="acard"><a href="%s.html"><span class="acard__img"><img src="../img/conseils/%s" width="800" height="533" alt="%s" loading="lazy" decoding="async"></span>'
            '<span class="acard__body"><span class="label acard__cat">%s</span><span class="acard__t">%s</span>%s<span class="acard__more">Lire l’article <span aria-hidden="true">→</span></span></span></a></li>'
            ) % (a['slug'], vignette(a), esc(alt), a['categorie'], a['h1'], '' if small else '<span class="acard__d">%s</span>' % a['description'])

for a in ARTICLES:
    url = '%s/conseils/%s' % (SITE, a['slug'])
    img, alt = a['image']
    # illustration animée (SVG) : image de partage en JPG, les réseaux sociaux ne lisent pas le SVG
    img_url = '%s/img/conseils/%s%s' % (SITE, img, '-og.jpg' if a.get('anim') else '.webp')
    toc = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', a['corps'])
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Article', 'headline': txt(a['h1']), 'description': a['description'], 'image': img_url, 'inLanguage': 'fr-FR',
         'datePublished': D[a['slug']]['publie'], 'dateModified': D[a['slug']]['maj'], 'author': {'@type': 'Organization', 'name': 'La rédaction de ' + NAME, 'url': SITE + '/a-propos'},
         'editor': {'@type': 'Person', 'name': 'Kesiah Ntumba', 'url': SITE + '/a-propos'}, 'publisher': ORG, 'mainEntityOfPage': url, 'articleSection': a['categorie']},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': r}} for q, r in a['faq']]},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Conseils', 'item': SITE + '/conseils'},
            {'@type': 'ListItem', 'position': 3, 'name': txt(a['h1']), 'item': url}]}]}
    cta = a['cta']
    main = '''<main id="contenu">
  <article class="art">
    <header class="wrap art__head">
      <nav class="art__crumbs" aria-label="Fil d’Ariane"><a href="../index.html">Accueil</a><span aria-hidden="true">/</span><a href="index.html">Conseils</a><span aria-hidden="true">/</span><span>%(cat)s</span></nav>
      <p class="eyebrow">%(cat)s</p>
      <h1>%(h1)s</h1>
      <p class="lead art__chapo">%(chapo)s</p>
      <p class="art__meta"><span>Par <a href="../a-propos.html">la rédaction de %(name)s</a></span><span>Relu par <a href="../a-propos.html#qui">Kesiah Ntumba</a></span><span>Mis à jour le %(maj)s</span><span>%(lecture)d&nbsp;min de lecture</span></p>
    </header>
    <figure class="wrap art__hero">
      %(hero)s
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
          <p class="art__cta-note">Les boutons vers augment.eco sont des liens partenaires&nbsp;: <a href="../a-propos.html#financement">comment le site est financé</a>.</p>
        </section>
        <section class="art__faq" aria-labelledby="faq-art"><h2 id="faq-art">Questions fréquentes</h2>%(faq)s</section>
        <section class="art__sources" aria-labelledby="src-art"><h2 id="src-art" class="label">Sources</h2><ul>%(sources)s</ul><p>Prix relevés sur augment.eco (France). <a href="../a-propos.html#methode">Notre méthode</a>.</p></section>
      </div>
    </div>
    <section class="wrap art__related" aria-labelledby="lies"><h2 id="lies">À lire aussi</h2><ul class="acards">%(lies)s</ul></section>
  </article>
</main>''' % dict(hero=('<img src="../img/conseils/%s.svg" width="1536" height="1024" alt="%s" fetchpriority="high">' % (img, esc(alt))) if a.get('anim') else
                      ('<img src="../img/conseils/%s.webp" srcset="../img/conseils/%s-800.webp 800w, ../img/conseils/%s.webp 1536w" sizes="(max-width: 1100px) 100vw, 1100px" width="1536" height="1024" alt="%s" fetchpriority="high">' % (img, img, img, esc(alt))),
                 cat=a['categorie'], h1=a['h1'], chapo=a['chapo'], name=NAME, maj=date_fr(D[a['slug']]['maj']), lecture=a['lecture'], img=img, alt=esc(alt),
                 toc=''.join('<a href="#%s">%s</a>' % (i, t) for i, t in toc),
                 bref=''.join('<li>%s</li>' % b for b in a['en_bref']), corps=a['corps'],
                 cta_t=cta['titre'], cta_x=cta['texte'], cta_b=''.join(cta['boutons']),
                 faq=''.join('<details class="hfaq__item"><summary><span class="hfaq__q">%s</span><span class="hfaq__icon" aria-hidden="true">+</span></summary><p class="hfaq__a">%s</p></details>' % (q.replace(' ?', '&nbsp;?'), r) for q, r in a['faq']),
                 sources=''.join('<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, t) for t, u in a['sources']),
                 lies=''.join(carte(BY[s], small=True) for s in a['lies'] if s in BY))
    html = page_head(a['titre_seo'], a['description'], seo_block(url, a['titre_seo'], a['description'], img_url, 'article', ld)) + absolutise(main, '/conseils/') + foot
    os.makedirs(ROOT + 'conseils', exist_ok=True)
    io.open(ROOT + 'conseils/%s.html' % a['slug'], 'w', encoding='utf-8', newline='').write(html)

# ---------- page d'accueil de la rubrique ----------
url = SITE + '/conseils'
title = 'Conseils trottinette et scooter électrique : guides pratiques'
desc = 'Louer ou acheter, assurance et règles, écologie, scooter 45 km/h : nos guides pratiques pour bien choisir et rouler sereinement en trottinette électrique.'
ld = {'@context': 'https://schema.org', '@graph': [
    {'@type': 'CollectionPage', 'name': title, 'url': url, 'description': desc, 'inLanguage': 'fr-FR', 'publisher': ORG,
     'hasPart': [{'@type': 'Article', 'headline': txt(a['h1']), 'url': '%s/conseils/%s' % (SITE, a['slug'])} for a in ARTICLES]},
    {'@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': 1, 'name': 'Accueil', 'item': SITE + '/'},
                                                    {'@type': 'ListItem', 'position': 2, 'name': 'Conseils', 'item': url}]}]}
main = '''<main id="contenu">
  <section class="wrap art__head art__head--list">
    <nav class="art__crumbs" aria-label="Fil d’Ariane"><a href="../index.html">Accueil</a><span aria-hidden="true">/</span><span>Conseils</span></nav>
    <p class="eyebrow">Conseils</p>
    <h1>Bien choisir, bien rouler.</h1>
    <p class="lead art__chapo">Des guides simples pour décider entre location et achat, rouler en règle et tirer le meilleur de votre trottinette ou de votre scooter électrique.</p>
  </section>
  <section class="wrap art__list" aria-label="Articles"><ul class="acards acards--big">%s</ul></section>
</main>''' % ''.join(carte(a) for a in ARTICLES)
html = page_head(title, desc, seo_block(url, title, desc, SITE + '/img/og.jpg', 'website', ld)) + absolutise(main, '/conseils/') + foot
io.open(ROOT + 'conseils/index.html', 'w', encoding='utf-8', newline='').write(html)
io.open(DATES_F, 'w', encoding='utf-8', newline='\n').write(json.dumps(D, indent=1, ensure_ascii=False, sort_keys=True))
print('%d articles + index générés' % len(ARTICLES))
