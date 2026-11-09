# -*- coding: utf-8 -*-
"""Propositions de logo et de favicon pour Roulelibre (rien n'est inséré dans le site).
    python tools/logo_propositions.py   ->  tools/logo/*.svg + tools/logo/propositions.html
Chaque piste : favicon (cercle plein, motif dans la zone sûre pour le rognage rond de Google),
logo du site (sans fond, déclinable clair / foncé) et page de comparaison."""
import os, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
OUT = ROOT + 'tools/logo/'
os.makedirs(OUT, exist_ok=True)

ACC, INK, CREAM, SUN, WHITE = '#FF5A1F', '#121412', '#FFF4EA', '#FFB547', '#FFFFFF'


def pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


# ---------------------------------------------------------------- A : roue ouverte + soleil
def a_glyph(ring, dot, hub, bw=None):
    """Roue en anneau ouvert en haut à droite (liberté), petit soleil dans l'ouverture."""
    cx, cy, r = 32, 35, 16
    circ = 2 * math.pi * r
    gap = circ * 0.19
    x, y = pt(cx, cy, r, -58)
    return ('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="8" stroke-linecap="round" stroke-dasharray="%.1f %.1f" transform="rotate(-23 %d %d)"/>'
            '<circle cx="%.1f" cy="%.1f" r="6.2" fill="%s"/><circle cx="%d" cy="%d" r="3.6" fill="%s"/>'
            % (cx, cy, r, ring, circ - gap, gap, cx, cy, x + 2.5, y - 2.5, dot, cx, cy, hub))


def a_fav():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="%s"/>%s</svg>'
            % (ACC, a_glyph(WHITE, SUN, WHITE)))


def a_mark(ring=ACC, dot=SUN, hub=INK):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="4 6 56 56">%s</svg>' % a_glyph(ring, dot, hub)


# ---------------------------------------------------------------- B : monogramme R
def b_letter(c, lines=None):
    s = ('<path d="M22 47 V17 H33 a9.2 9.2 0 0 1 0 18.4 H22 M32 35.4 L42.5 47" fill="none" stroke="%s" stroke-width="7.4" stroke-linecap="round" stroke-linejoin="round"/>' % c)
    if lines:
        s += ('<path d="M8 26 h8 M11 36 h5" fill="none" stroke="%s" stroke-width="4.2" stroke-linecap="round"/>' % lines)
    return s


def b_fav():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="%s"/><g transform="translate(1.5 0)">%s</g></svg>'
            % (ACC, b_letter(WHITE)))


def b_mark():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="19" fill="%s"/><g transform="translate(3 0)">%s</g>'
            '<circle cx="52" cy="14" r="5" fill="%s"/></svg>' % (ACC, b_letter(WHITE, SUN), SUN))


# ---------------------------------------------------------------- C : trottinette
def c_glyph(body, wheel, sun, hub=None):
    return ('<path d="M17 45 H44 L38.5 15.5 H46" fill="none" stroke="%s" stroke-width="5.4" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="17.5" cy="47" r="6.6" fill="%s"/><circle cx="46" cy="47" r="6.6" fill="%s"/>'
            '<circle cx="17.5" cy="47" r="2.3" fill="%s"/><circle cx="46" cy="47" r="2.3" fill="%s"/>'
            '<circle cx="20" cy="22" r="6" fill="%s"/>' % (body, wheel, wheel, hub or body, hub or body, sun))


def c_fav():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="%s"/>%s</svg>'
            % (ACC, c_glyph(WHITE, WHITE, SUN, ACC)))


def c_mark(body=INK, wheel=ACC, sun=SUN, hub=CREAM):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="8 8 46 46">%s</svg>' % c_glyph(body, wheel, sun, hub)


PISTES = [
    dict(id='a', nom='A · La roue libre', idee='Une roue dont l’anneau reste ouvert : le mouvement, la liberté, et un petit soleil qui s’échappe. Rond, simple, très lisible en minuscule.',
         fav=a_fav(), mark=a_mark(), mark_dark=a_mark(ring=ACC, dot=SUN, hub=CREAM),
         wm=lambda col: '<b>Roule<span style="color:#FF5A1F">libre</span></b>', wm_col=INK),
    dict(id='b', nom='B · Le monogramme R', idee='Un R géométrique, épais et chaleureux, avec deux traits de vitesse et un soleil. Se reconnaît tout de suite, même à 16 pixels.',
         fav=b_fav(), mark=b_mark(), mark_dark=b_mark(),
         wm=lambda col: '<b>Roulelibre</b>', wm_col=INK),
    dict(id='c', nom='C · La trottinette', idee='Le véhicule lui-même, dessiné en un seul trait épais : guidon, plateau, deux roues, et un soleil au-dessus. Le plus parlant, le plus « mobilité ».',
         fav=c_fav(), mark=c_mark(), mark_dark=c_mark(body=CREAM, hub=INK),
         wm=lambda col: '<b>roulelibre</b>', wm_col=INK),
]

for p in PISTES:
    open(OUT + p['id'] + '-favicon.svg', 'w', encoding='utf-8', newline='\n').write(p['fav'])
    open(OUT + p['id'] + '-logo.svg', 'w', encoding='utf-8', newline='\n').write(p['mark'])
    open(OUT + p['id'] + '-logo-sombre.svg', 'w', encoding='utf-8', newline='\n').write(p['mark_dark'])


def img(name, h, extra=''):
    return '<img src="%s" height="%d" alt="" %s>' % (name, h, extra)


def lockup(p, dark=False, h=42, tag=True):
    mk = p['id'] + ('-logo-sombre.svg' if dark else '-logo.svg')
    wm = p['wm'](None)
    cls = 'lk lk--dark' if dark else 'lk'
    return ('<span class="%s"><img src="%s" height="%d" alt=""><span class="lk__t">%s%s</span></span>'
            % (cls, mk, h, wm, '<small>Mobilité électrique</small>' if tag else ''))


def serp(p):
    return ('<div class="serp"><div class="serp__top"><span class="serp__ico"><img src="%s-favicon.svg" alt=""></span>'
            '<span class="serp__site"><b>Roulelibre</b><i>https://roulelibre.fr</i></span></div>'
            '<div class="serp__t">Location trottinette électrique longue durée : Augment Agaru</div>'
            '<div class="serp__d">Louez ou achetez une trottinette électrique ou un scooter pliable, réparations comprises. Prix relevés sur augment.eco.</div></div>') % p['id']


def tab(p):
    return ('<div class="tab"><span class="tab__i"><img src="%s-favicon.svg" alt=""></span><span>Roulelibre | Mobilité électrique</span></div>') % p['id']


rows = ''
for p in PISTES:
    sizes = ''.join('<figure><img src="%s-favicon.svg" width="%d" height="%d" alt=""><figcaption>%d px</figcaption></figure>' % (p['id'], s, s, s) for s in (16, 24, 32, 48, 96))
    rows += '''
<section class="piste">
  <header><h2>%(nom)s</h2><p>%(idee)s</p></header>
  <div class="grid">
    <div class="card"><h3>Logo sur le site (fond crème)</h3><div class="demo demo--cream">%(lk_light)s</div><div class="demo demo--cream big">%(lk_big)s</div></div>
    <div class="card"><h3>Logo sur fond sombre (pied de page)</h3><div class="demo demo--dark">%(lk_dark)s</div><div class="demo demo--orange">%(lk_orange)s</div></div>
    <div class="card"><h3>Favicon : tailles réelles</h3><div class="sizes">%(sizes)s</div><h3 class="mt">Onglet du navigateur</h3>%(tab)s</div>
    <div class="card"><h3>Résultat Google (rond)</h3>%(serp)s</div>
  </div>
</section>''' % dict(nom=p['nom'], idee=p['idee'], lk_light=lockup(p), lk_big=lockup(p, h=64), lk_dark=lockup(p, dark=True), lk_orange='<img src="%s-favicon.svg" height="56" alt=""> <img src="%s-favicon.svg" height="40" alt=""> <img src="%s-favicon.svg" height="28" alt="">' % ((p['id'],) * 3),
                       sizes=sizes, tab=tab(p), serp=serp(p), **{})


# ---------------------------------------------------------------- pistes Codex (images, recadrées par un script séparé)
CODEX = [('d-oiseau-roue', 'D · L’oiseau-roue', 'Un oiseau en vol dont la queue s’enroule en roue : « libre » et « roule » dans un seul dessin. Le plus expressif, mais plus détaillé à 16 px.'),
         ('e-lever-soleil', 'E · Lever de soleil', 'Une roue devant un demi-soleil. Très simple et lisible, mais proche d’une Pokéball.'),
         ('f-r-roue', 'F · Le r-roue', 'Le r dont le bras devient une roue. À écarter : il se lit « p » ou « b ».'),
         ('g-trottinette-mouvement', 'G · Trottinette en mouvement', 'Une trottinette avec un visage souriant et des traits de vitesse. Sympathique, mais plus mascotte que logo.'),
         ('h-ruban-route', 'H · Ruban de route', 'Route, roue et flèche en un seul trait. Trop chargé pour une petite taille.')]
crow = ''
for cid, nom, idee in CODEX:
    sizes = ''.join('<figure><img src="codex/%s-favicon.png" width="%d" height="%d" alt=""><figcaption>%d px</figcaption></figure>' % (cid, s, s, s) for s in (16, 24, 32, 48, 96))
    crow += """
<section class="piste">
  <header><h2>%s</h2><p>%s</p></header>
  <div class="grid">
    <div class="card"><h3>Logo (fond crème et sombre)</h3><div class="demo demo--cream"><img src="codex/%s-logo.png" height="96" alt=""><img src="codex/%s-logo.png" height="40" alt=""></div><div class="demo demo--dark"><img src="codex/%s-logo.png" height="48" alt="" style="border-radius:8px"></div></div>
    <div class="card"><h3>Favicon : tailles réelles</h3><div class="sizes">%s</div><h3 class="mt">Onglet du navigateur</h3><div class="tab"><span class="tab__i"><img src="codex/%s-favicon.png" alt=""></span><span>Roulelibre | Mobilité électrique</span></div></div>
    <div class="card"><h3>Image d’origine (Codex)</h3><img src="codex/%s.png" style="width:100%%;border-radius:10px" alt=""></div>
  </div>
</section>""" % (nom, idee, cid, cid, cid, sizes, cid, cid)

html = '''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>Roulelibre : propositions de logo et de favicon</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Geist:wght@400..700&family=Geist+Mono:wght@400..600&display=swap">
<style>
:root{--paper:#EFEDE6;--ink:#121412;--muted:#5C605B;--line:#D9D5CA;--acc:#FF5A1F}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Geist,system-ui,sans-serif;line-height:1.5}
.page{max-width:1280px;margin:0 auto;padding:32px 24px 80px}
h1{font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(30px,4vw,48px);letter-spacing:-.025em;margin:0 0 6px}
.lead{color:var(--muted);max-width:70ch;margin:0 0 36px}
.piste{margin-top:44px;padding-top:28px;border-top:2px solid var(--ink)}
.piste h2{font-family:'Bricolage Grotesque',sans-serif;font-size:28px;margin:0 0 4px;letter-spacing:-.02em}.piste header p{margin:0 0 20px;color:var(--muted);max-width:75ch}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:18px}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px}
.card h3{font:500 11.5px 'Geist Mono',monospace;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}.mt{margin-top:22px!important}
.demo{border-radius:12px;padding:18px 20px;margin-bottom:10px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.demo--cream{background:var(--paper)}.demo--dark{background:#121412}.demo--orange{background:#FF5A1F;gap:18px}.demo.big{padding:26px 20px}
.lk{display:inline-flex;align-items:center;gap:11px}.lk__t{display:flex;flex-direction:column;line-height:1.05}
.lk b{font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:22px;letter-spacing:-.02em;color:#121412}
.lk small{font:10.5px 'Geist Mono',monospace;letter-spacing:.06em;text-transform:uppercase;color:#5C605B;margin-top:3px}
.lk--dark b{color:#fff}.lk--dark small{color:#8E918A}
.big .lk b{font-size:34px}.big .lk small{font-size:13px}
.sizes{display:flex;gap:22px;align-items:flex-end;flex-wrap:wrap}.sizes figure{margin:0;text-align:center}.sizes figcaption{font:11px 'Geist Mono',monospace;color:var(--muted);margin-top:6px}
.tab{display:inline-flex;align-items:center;gap:8px;background:#DEE1E6;border-radius:10px 10px 0 0;padding:9px 16px;font:13px Arial,sans-serif;color:#202124}.tab__i img{width:16px;height:16px;display:block}
.serp{font-family:Arial,sans-serif;max-width:560px}.serp__top{display:flex;align-items:center;gap:12px;margin-bottom:4px}
.serp__ico{width:28px;height:28px;border-radius:50%;background:#F1F3F4;display:grid;place-items:center;overflow:hidden;flex:none}.serp__ico img{width:18px;height:18px;display:block}
.serp__site{display:flex;flex-direction:column;line-height:1.25}.serp__site b{font-weight:400;font-size:14px;color:#202124}.serp__site i{font-style:normal;font-size:12px;color:#4D5156}
.serp__t{font-size:20px;line-height:1.3;color:#1A0DAB;margin:2px 0 3px}.serp__d{font-size:14px;line-height:1.58;color:#4D5156}
@media (prefers-color-scheme:dark){}
</style></head><body><div class="page">
<h1>Logo et favicon : 8 pistes</h1>
<p class="lead">Chaque piste a un favicon rond (le motif reste dans la zone centrale, pour que Google, qui rogne en cercle, ne coupe rien) et un logo pour le site, sans obligation de cercle. Les trois sont en orange du site, avec un soleil jaune pour le côté joyeux. A, B, C : dessinées en vectoriel (SVG, nettes à toutes les tailles). D à H : générées par Codex (images, à vectoriser si la piste est retenue). Rien n’est encore inséré dans les pages.</p>
@@ROWS@@
</div></body></html>'''.replace('@@ROWS@@', rows + crow)

open(OUT + 'propositions.html', 'w', encoding='utf-8', newline='\n').write(html)
print('ok', os.listdir(OUT))
