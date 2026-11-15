# -*- coding: utf-8 -*-
"""Illustrations animées (SVG + CSS, sans JavaScript) des articles de la rubrique Conseils.
    python tools/illustrations_conseils.py [identifiant ...]   ->  img/conseils/anim-<id>.svg  +  anim-<id>-og.jpg
Même univers que l'illustration « forfait mobilités durables » (tools/illustration_fmd.py) : ville ensoleillée, tons chauds,
couleurs de css/style.css. Les animations s'arrêtent si le visiteur a demandé moins d'animations (prefers-reduced-motion).
Les véhicules sont des silhouettes génériques (illustration), pas une représentation exacte d'un modèle."""
import os, sys, math, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
OUT = ROOT + 'img/conseils/'
W, H = 1536, 1024

ACCENT, INK, CREAM = '#FF5A1F', '#2B2E2B', '#FFF4EA'
SUN, PEACH, CORAL = '#FFB547', '#FFC7A6', '#FF9466'
TEAL, TEAL_D = '#2F7A6B', '#22594E'
MUSTARD, NAVY, SKIN, SKIN2 = '#F2A93B', '#23304A', '#A8673F', '#E2A878'
GROUND = 947          # ligne de contact des roues


# ----------------------------------------------------------------------------------------------- décor
def skyline(rnd, base, hmin, hmax, wmin, wmax, colors, win, gap=6, round_top=False):
    out, x = [], 0
    while x < W:
        w = rnd.randint(wmin, wmax)
        w = min(w, W - x) if W - x < wmin + 20 else w
        h = rnd.randint(hmin, hmax)
        c = rnd.choice(colors)
        out.append('<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s"/>' % (x, base - h, w, h + 40, 14 if round_top else 6, c))
        if win:
            for wy in range(base - h + 26, base - 30, 38):
                for wx in range(x + 16, x + w - 24, 30):
                    if rnd.random() < .78:
                        out.append('<rect x="%d" y="%d" width="12" height="18" rx="3" fill="%s"/>' % (wx, wy, win))
        x += w + gap
    g = ''.join(out)
    return '<g>%s</g><g transform="translate(%d 0)">%s</g>' % (g, W, g)


def trees(rnd, base, greens=(TEAL, '#3E8C72', TEAL_D)):
    out, x = [], 40
    while x < W - 40:
        h, r = rnd.randint(90, 130), rnd.randint(46, 62)
        c = rnd.choice(greens)
        out.append('<rect x="%d" y="%d" width="10" height="%d" rx="4" fill="#7A4A2B"/>' % (x - 5, base - h + r, h - r))
        out.append('<g class="sway" style="animation-delay:-%.1fs"><circle cx="%d" cy="%d" r="%d" fill="%s"/><circle cx="%d" cy="%d" r="%d" fill="#5FA88A" opacity=".55"/></g>'
                   % (rnd.random() * 3, x, base - h, r, c, x - r * .35, base - h - r * .3, r * .45))
        x += rnd.randint(240, 330)
    g = ''.join(out)
    return '<g>%s</g><g transform="translate(%d 0)">%s</g>' % (g, W, g)


def cloud(x, y, s, fill=CREAM):
    return ('<g transform="translate(%d %d) scale(%.2f)"><ellipse rx="70" ry="30" fill="%s"/>'
            '<circle cx="-28" cy="-18" r="32" fill="%s"/><circle cx="22" cy="-26" r="40" fill="%s"/></g>') % (x, y, s, fill, fill, fill)


def clouds_loop(pts, fill=CREAM):
    one = ''.join(cloud(x, y, s, fill) for x, y, s in pts)
    return '<g class="clouds">%s<g transform="translate(%d 0)">%s</g></g>' % (one, W, one)


def wheel(cx, cy, r=42, spin=True):
    k = r / 42.0
    spokes = ''.join('<line x1="0" y1="0" x2="%.1f" y2="%.1f" stroke="#8A8D86" stroke-width="4" stroke-linecap="round"/>'
                     % (24 * math.cos(a * 1.0472), 24 * math.sin(a * 1.0472)) for a in range(6))
    return ('<g transform="translate(%d %d) scale(%.3f)"><g class="%s"><circle r="42" fill="#121412"/><circle r="30" fill="#3A3D3A"/>%s'
            '<circle r="8" fill="%s"/></g></g>') % (cx, cy, k, 'wheel' if spin else '', spokes, ACCENT)


def place(inner, x, s=1.0, dy=0):
    """Pose un véhicule dessiné autour de x=760, au sol y=947, centré sur x."""
    return '<g transform="translate(%.1f %.1f) scale(%.3f) translate(-760 -%d)">%s</g>' % (x, GROUND + dy, s, GROUND, inner)


def sun(cx=1190, cy=250, r=130):
    rays = ''.join('<rect x="-7" y="-%d" width="14" height="44" rx="7" fill="%s" transform="rotate(%d)"/>' % (r + 66, SUN, a) for a in range(0, 360, 30))
    return ('<g transform="translate(%d %d)"><g class="rays">%s</g></g><circle class="sun-core" style="transform-origin:%dpx %dpx" cx="%d" cy="%d" r="%d" fill="%s"/>'
            '<circle cx="%d" cy="%d" r="%d" fill="#FFC769"/>') % (cx, cy, rays, cx, cy, cx, cy, r, SUN, cx, cy, int(r * .74))


# ----------------------------------------------------------------------------------------------- véhicules
def kick(shirt=TEAL, shirt_d=TEAL_D, helmet=ACCENT, pants=NAVY, bag=MUSTARD, rider=True, scarf=ACCENT, coat=False):
    """Trottinette électrique (silhouette) et, si rider, son conducteur."""
    s = '''<g class="rider">
 <rect x="618" y="880" width="262" height="20" rx="10" fill="#121412"/>
 <path d="M612 880 q-6 -28 22 -30 h20" fill="none" stroke="#121412" stroke-width="12" stroke-linecap="round"/>
 <line x1="848" y1="612" x2="884" y2="900" stroke="#121412" stroke-width="16" stroke-linecap="round"/>
 <line x1="818" y1="606" x2="886" y2="618" stroke="#121412" stroke-width="12" stroke-linecap="round"/>
 <circle cx="851" cy="622" r="6" fill="%(ACCENT)s"/><circle cx="626" cy="876" r="7" fill="#FF3B2F"/>
 %(w1)s %(w2)s''' % dict(ACCENT=ACCENT, w1=wheel(640, 905), w2=wheel(880, 905))
    if rider:
        s += '''
 <path d="M742 700 L712 790 L702 872" fill="none" stroke="%(pants)s" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
 <path d="M760 700 L798 784 L792 872" fill="none" stroke="%(pants)s" stroke-width="34" stroke-linecap="round" stroke-linejoin="round" opacity=".85"/>
 <path d="M680 868 h44 q8 0 8 10 h-60 q0 -10 8 -10z" fill="#FFFFFF"/><path d="M772 868 h44 q8 0 8 10 h-60 q0 -10 8 -10z" fill="#FFFFFF"/>
 <rect x="694" y="566" width="62" height="104" rx="22" fill="%(bag)s" transform="rotate(14 725 618)"/>
 <path d="M720 712 L788 712 L826 584 Q812 540 768 544 L734 566 Z" fill="%(shirt)s"/>
 <path d="M770 548 L800 556 L788 712 L760 712 Z" fill="%(shirt_d)s" opacity=".35"/>
 <path d="M800 572 L836 612 L850 614" fill="none" stroke="%(shirt)s" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="852" cy="614" r="13" fill="%(SKIN)s"/>
 <g class="scarf"><path d="M806 548 C770 556 740 552 712 540 L716 560 C744 572 774 574 804 566 Z" fill="%(scarf)s"/></g>
 <rect x="784" y="520" width="26" height="34" rx="10" fill="%(SKIN)s"/>
 <circle cx="800" cy="492" r="38" fill="%(SKIN)s"/>
 <path d="M760 488 a41 41 0 0 1 82 -6 l14 6 q4 4 -2 7 l-94 4 z" fill="%(helmet)s"/>
 <path d="M776 470 a30 30 0 0 1 40 -14" fill="none" stroke="#FFFFFF" stroke-opacity=".45" stroke-width="7" stroke-linecap="round"/>
 <circle cx="822" cy="502" r="4.5" fill="#121412"/><path d="M812 520 q10 7 20 0" fill="none" stroke="#121412" stroke-width="4" stroke-linecap="round"/>''' % dict(
            pants=pants, bag=bag, shirt=shirt, shirt_d=shirt_d, SKIN=SKIN, scarf=scarf, helmet=helmet)
    return s + '</g>'


def moped(shirt=NAVY, helmet=ACCENT, pants='#3A3D3A', rider=True):
    """Scooter électrique pliable (silhouette : cadre gris, colonne batterie noire, selle, grosses roues) et son pilote assis."""
    s = '''<g class="rider">
 <rect x="596" y="868" width="150" height="22" rx="11" fill="#2A2D31"/>
 <path d="M690 880 Q740 934 820 900 L846 872 L806 858 Q760 892 704 850 Z" fill="#5A6068"/>
 <rect x="598" y="636" width="96" height="236" rx="26" fill="#1C1E22"/>
 <rect x="578" y="618" width="170" height="30" rx="15" fill="#121412"/>
 <rect x="572" y="626" width="9" height="20" rx="4" fill="#FF3B2F"/>
 <line x1="846" y1="872" x2="906" y2="650" stroke="#5A6068" stroke-width="26" stroke-linecap="round"/>
 <line x1="906" y1="650" x2="904" y2="892" stroke="#1C1E22" stroke-width="14" stroke-linecap="round"/>
 <line x1="872" y1="640" x2="946" y2="652" stroke="#121412" stroke-width="12" stroke-linecap="round"/>
 <line x1="878" y1="640" x2="868" y2="604" stroke="#121412" stroke-width="5"/><circle cx="866" cy="596" r="12" fill="#2A2D31"/><circle cx="866" cy="596" r="7" fill="#9BB8C4"/>
 <rect x="918" y="662" width="12" height="40" rx="6" fill="#FFE9A8" opacity=".9"/>
 <circle cx="606" cy="884" r="9" fill="%(ACCENT)s"/>
 <path d="M594 880 L560 892 L590 906 Z" fill="#2A2D31"/>
 %(w1)s %(w2)s''' % dict(ACCENT=ACCENT, w1=wheel(640, 892, 58), w2=wheel(904, 892, 58))
    if rider:
        s += '''
 <path d="M672 628 L790 690 L800 842" fill="none" stroke="%(pants)s" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>
 <path d="M786 838 h58 q10 0 10 12 h-78 z" fill="#FFFFFF"/>
 <path d="M668 640 L690 548 Q708 506 752 514 L790 540 L776 640 Z" fill="%(shirt)s"/>
 <path d="M770 540 L836 596 L930 646" fill="none" stroke="%(shirt)s" stroke-width="28" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="934" cy="648" r="14" fill="%(SKIN)s"/>
 <rect x="750" y="478" width="26" height="40" rx="10" fill="%(SKIN)s"/>
 <circle cx="770" cy="452" r="38" fill="%(SKIN)s"/>
 <path d="M728 448 a41 41 0 0 1 84 -8 l12 8 q4 4 -2 7 l-94 4 z" fill="%(helmet)s"/>
 <circle cx="794" cy="462" r="4.5" fill="#121412"/><path d="M782 480 q10 7 20 0" fill="none" stroke="#121412" stroke-width="4" stroke-linecap="round"/>''' % dict(
            pants=pants, shirt=shirt, helmet=helmet, SKIN=SKIN)
    return s + '</g>'


def standing(shirt=TEAL, pants=NAVY, helmet=None, hair='#3B2416', skin=SKIN):
    """Personne debout (de profil, tournée vers la droite), tête et jambes qui bougent légèrement. Centrée sur x=760, pieds au sol 947."""
    h = ('<path d="M732 408 a40 40 0 0 1 80 -6 l8 6 q2 4 -2 6 l-86 4 z" fill="%s"/>' % helmet) if helmet else '<path d="M730 450 a42 42 0 0 1 84 -2 q-4 -26 -42 -28 q-36 0 -42 30z" fill="%s"/>' % hair
    return '''<g class="walker">
 <path d="M748 700 L736 830 L730 936" fill="none" stroke="%(pants)s" stroke-width="32" stroke-linecap="round"/>
 <path d="M772 700 L792 826 L808 936" fill="none" stroke="%(pants)s" stroke-width="32" stroke-linecap="round" opacity=".85"/>
 <path d="M712 936 h44 q8 0 8 11 h-58 z" fill="#FFFFFF"/><path d="M790 936 h44 q8 0 8 11 h-58 z" fill="#FFFFFF"/>
 <path d="M724 712 L798 712 L812 548 Q790 506 748 516 L728 548 Z" fill="%(shirt)s"/>
 <rect x="756" y="480" width="26" height="40" rx="10" fill="%(skin)s"/>
 <circle cx="772" cy="450" r="38" fill="%(skin)s"/>%(h)s
 <circle cx="796" cy="458" r="4.5" fill="#121412"/><path d="M784 476 q10 7 20 0" fill="none" stroke="#121412" stroke-width="4" stroke-linecap="round"/>
</g>''' % dict(pants=pants, shirt=shirt, skin=skin, h=h)


def shadow(cx, rx=190):
    return '<ellipse cx="%d" cy="950" rx="%d" ry="14" fill="#121412" opacity=".33"/>' % (cx, rx)


# ----------------------------------------------------------------------------------------------- squelette commun
CSS_BASE = '''
.scroll-slow{animation:scroll 70s linear infinite}
.scroll-mid{animation:scroll 26s linear infinite}
.scroll-fast{animation:scroll 11s linear infinite}
.clouds{animation:scroll 120s linear infinite}
@keyframes scroll{to{transform:translateX(-%(W)dpx)}}
.rays{transform-origin:0 0;animation:spin 40s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.sun-core{animation:pulse 4s ease-in-out infinite}
@keyframes pulse{50%%{transform:scale(1.04)}}
.dash{animation:dash .55s linear infinite}
@keyframes dash{to{stroke-dashoffset:-120}}
.wheel{animation:spin .5s linear infinite}
.rider{animation:bob .9s ease-in-out infinite}
@keyframes bob{50%%{transform:translateY(-5px)}}
.scarf{transform-origin:806px 548px;animation:flap .45s ease-in-out infinite alternate}
@keyframes flap{to{transform:rotate(-9deg) scaleX(1.08)}}
.sway{transform-box:fill-box;transform-origin:50%% 100%%;animation:sway 3.2s ease-in-out infinite alternate}
@keyframes sway{from{transform:rotate(-2deg)}to{transform:rotate(2deg)}}
.speed line{animation:speed 1.1s linear infinite}
.speed line:nth-child(2){animation-delay:-.35s}.speed line:nth-child(3){animation-delay:-.7s}
@keyframes speed{0%%{transform:translateX(40px);opacity:0}30%%{opacity:.9}100%%{transform:translateX(-160px);opacity:0}}
.bird{animation:bird 30s linear infinite}
@keyframes bird{from{transform:translate(1600px,0)}to{transform:translate(-200px,-60px)}}
.float{animation:float 4.5s ease-in-out infinite}
@keyframes float{50%%{transform:translateY(-14px)}}
.walker{animation:bob .8s ease-in-out infinite}
'''

REDUCED = '@media (prefers-reduced-motion:reduce){*{animation:none!important}%s}'


def scene(ident, titre, rnd_seed, extra_css='', front='', reduced='', sky=('#FFD7BE', '#FFEBDC', '#FFF4EA'), sun_pos=(1190, 250),
          back_cols=(PEACH, '#FFBE98', '#FFD0B5'), mid_cols=(CORAL, ACCENT, '#E8693A', '#3A3D3A'), road_scroll=True,
          show_sun=True, cloud_fill=CREAM, tree_cols=(TEAL, '#3E8C72', TEAL_D), cloud_pts=None, deco=''):
    rnd = random.Random(rnd_seed)
    cp = cloud_pts or [(180, 120, 1.0), (620, 200, .8), (980, 110, .7), (1400, 180, 1.1)]
    mid = 'scroll-mid' if road_scroll else ''
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %(W)d %(H)d" width="%(W)d" height="%(H)d" role="img" aria-labelledby="t">
<title id="t">%(titre)s</title>
<style>%(css)s%(extra)s
%(reduced)s</style>
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%(s0)s"/><stop offset=".65" stop-color="%(s1)s"/><stop offset="1" stop-color="%(s2)s"/></linearGradient></defs>
<rect width="%(W)d" height="%(H)d" fill="url(#sky)"/>
%(sun)s
%(clouds)s
<g class="bird"><path d="M0 120 q14 -14 28 0 q14 -14 28 0" fill="none" stroke="%(INK)s" stroke-width="5" stroke-linecap="round"/><path d="M70 150 q10 -10 20 0 q10 -10 20 0" fill="none" stroke="%(INK)s" stroke-width="4" stroke-linecap="round"/></g>
<g class="scroll-slow">%(back)s</g>
<g class="%(mid)s">%(midl)s</g>
<rect y="760" width="%(W)d" height="60" fill="#F6CDB4"/><rect y="812" width="%(W)d" height="10" fill="#E9B394"/>
<g class="%(mid)s">%(trees)s</g>
<rect y="822" width="%(W)d" height="202" fill="%(INK)s"/><rect y="838" width="%(W)d" height="6" fill="%(ACCENT)s"/>
<line class="%(dashc)s" x1="0" y1="985" x2="%(W)d" y2="985" stroke="#FFE6DA" stroke-width="10" stroke-dasharray="70 50"/>
%(deco)s
%(front)s
</svg>
''' % dict(W=W, H=H, titre=titre, css=CSS_BASE % dict(W=W), extra=extra_css, reduced=REDUCED % reduced, s0=sky[0], s1=sky[1], s2=sky[2],
           sun=sun(sun_pos[0], sun_pos[1]) if show_sun else '', clouds=clouds_loop(cp, cloud_fill), INK=INK, ACCENT=ACCENT,
           back=skyline(rnd, 760, 220, 400, 110, 190, list(back_cols), '#FFE3D2', gap=10, round_top=True),
           midl=skyline(rnd, 770, 120, 260, 90, 160, list(mid_cols), '#FFE6DA', gap=24),
           trees=trees(rnd, 800, tree_cols), mid=mid, dashc='dash' if road_scroll else '', deco=deco, front=front)


def txt(x, y, s, size=34, fill='#FFFFFF', weight=700, anchor='middle'):
    return '<text x="%s" y="%s" text-anchor="%s" font-family="Arial, Helvetica, sans-serif" font-weight="%d" font-size="%d" fill="%s">%s</text>' % (x, y, anchor, weight, size, fill, s)


# ----------------------------------------------------------------------------------------------- les scènes
def s_louer_acheter():
    css = '''
.beam{transform-origin:768px 330px;animation:tilt 6s ease-in-out infinite alternate}
@keyframes tilt{from{transform:rotate(-7deg)}to{transform:rotate(7deg)}}
.panL{animation:panL 6s ease-in-out infinite alternate}.panR{animation:panR 6s ease-in-out infinite alternate}
@keyframes panL{from{transform:translateY(27px)}to{transform:translateY(-27px)}}
@keyframes panR{from{transform:translateY(-27px)}to{transform:translateY(27px)}}
.coinp{animation:float 3s ease-in-out infinite}.coinp:nth-child(2){animation-delay:-1s}.coinp:nth-child(3){animation-delay:-2s}
'''
    coin = lambda x, y, d: '<g class="coinp" style="animation-delay:%ss"><circle cx="%d" cy="%d" r="27" fill="#FFC23D" stroke="#E8941C" stroke-width="5"/>%s</g>' % (d, x, y, txt(x, y + 11, '€', 32, '#A85A0A'))
    pan = lambda cx, inner: ('<line x1="%d" y1="338" x2="%d" y2="560" stroke="%s" stroke-width="5"/><line x1="%d" y1="338" x2="%d" y2="560" stroke="%s" stroke-width="5"/>'
                             '<path d="M%d 560 h260 q-20 70 -130 70 q-110 0 -130 -70z" fill="%s"/>%s') % (cx - 120, cx - 20, INK, cx + 120, cx + 20, INK, cx - 130, ACCENT, inner)
    gauche = '<g transform="translate(%d %d) scale(.5)">%s</g>' % (108, 83, kick(rider=False).replace('class="rider"', 'class=""'))
    f = '''<rect x="754" y="330" width="28" height="520" rx="10" fill="%(INK)s"/><rect x="660" y="830" width="216" height="26" rx="13" fill="%(INK)s"/>
<g class="panL">%(pl)s</g><g class="panR">%(pr)s</g>
<g class="beam"><rect x="368" y="322" width="800" height="18" rx="9" fill="%(INK)s"/><circle cx="768" cy="331" r="22" fill="%(ACC)s"/><circle cx="768" cy="331" r="8" fill="%(CR)s"/></g>''' % dict(
        INK=INK, ACC=ACCENT, CR=CREAM, pl=pan(488, gauche), pr=pan(1048, coin(1000, 536, 0) + coin(1048, 520, 1) + coin(1100, 536, 2)))
    rid = place(kick(), 190, .72)
    return scene('louer-acheter', 'Illustration animée : une balance hésite entre une trottinette électrique et des pièces en euros, pendant qu’une personne roule au soleil',
                 11, css, f + rid)


def s_assurance():
    css = '''
.shield{transform-origin:768px 330px;animation:shield 3.6s ease-in-out infinite}
@keyframes shield{50%{transform:scale(1.05) translateY(-8px)}}
.tick{stroke-dasharray:260;stroke-dashoffset:260;animation:tick 3.6s ease-in-out infinite}
@keyframes tick{0%,15%{stroke-dashoffset:260}45%,85%{stroke-dashoffset:0}100%{stroke-dashoffset:260}}
.glint{animation:glint 3.6s ease-in-out infinite}
@keyframes glint{0%,100%{opacity:0;transform:translateX(-80px)}50%{opacity:.8;transform:translateX(70px)}}
.sign{transform-origin:200px 840px;animation:sway 3s ease-in-out infinite alternate}
.spark{animation:spark 2.4s ease-in-out infinite}.spark:nth-of-type(2){animation-delay:-.8s}.spark:nth-of-type(3){animation-delay:-1.6s}
@keyframes spark{0%,100%{opacity:0;transform:scale(.4)}50%{opacity:1;transform:scale(1)}}
'''
    star = lambda x, y, d: '<g class="spark" style="transform-origin:%dpx %dpx;animation-delay:%ss"><path d="M%d %d l8 -22 l8 22 l22 8 l-22 8 l-8 22 l-8 -22 l-22 -8z" fill="#FFC23D"/></g>' % (x, y, d, x - 8, y - 8)
    f = '''<g class="sign"><rect x="194" y="560" width="12" height="270" rx="5" fill="#7A8084"/>
<circle cx="200" cy="520" r="78" fill="#FFFFFF" stroke="#E5322D" stroke-width="16"/>%(t25)s</g>
<g class="shield"><path d="M768 160 L930 214 V360 Q930 470 768 540 Q606 470 606 360 V214 Z" fill="%(TEAL)s"/>
<path d="M768 160 L930 214 V360 Q930 470 768 540 Z" fill="%(TD)s" opacity=".35"/>
<path d="M768 190 L904 236 V358 Q904 446 768 508 Q632 446 632 358 V236 Z" fill="none" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="6"/>
<path class="tick" d="M690 350 L752 412 L852 290" fill="none" stroke="#FFFFFF" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
<rect class="glint" x="660" y="200" width="46" height="320" fill="#FFFFFF" opacity="0" transform="rotate(18 768 360)"/></g>
%(s1)s%(s2)s%(s3)s%(sh)s%(r)s''' % dict(TEAL=TEAL, TD=TEAL_D, t25=txt(200, 546, '25', 64, INK, 800), s1=star(560, 220, 0), s2=star(1000, 300, .8), s3=star(1070, 190, 1.6),
                                       sh=shadow(980, 190), r=place(kick(shirt=NAVY, helmet=MUSTARD), 1010, 1.0))
    return scene('assurance', 'Illustration animée : un bouclier protecteur validé par une coche, un panneau de vitesse et une personne casquée en trottinette électrique',
                 12, css, f, '.tick{stroke-dashoffset:0}', sun_pos=(1330, 170))


def s_ecologie():
    css = '''
.blades{transform-origin:330px 330px;animation:spin 7s linear infinite}
.leaf{animation:leaf 9s linear infinite;opacity:0}
.leaf:nth-of-type(2){animation-delay:-2.5s}.leaf:nth-of-type(3){animation-delay:-5s}.leaf:nth-of-type(4){animation-delay:-7s}
@keyframes leaf{0%{opacity:0;transform:translate(1500px,160px) rotate(0)}10%{opacity:1}90%{opacity:1}100%{opacity:0;transform:translate(-120px,520px) rotate(540deg)}}
.co2{animation:co2 6s ease-in infinite}.co2:nth-of-type(2){animation-delay:-3s}
@keyframes co2{0%{opacity:.7;transform:translate(0,0) scale(1)}100%{opacity:0;transform:translate(-120px,-70px) scale(.3)}}
.heart{transform-origin:1105px 430px;animation:pulse 1.6s ease-in-out infinite}
'''
    leaf = lambda c: '<g class="leaf"><path d="M0 0 q26 -34 62 -28 q-2 38 -34 56 q-12 -10 -28 -28z" fill="%s"/><path d="M4 -2 q26 4 52 -22" stroke="#FFFFFF" stroke-opacity=".5" stroke-width="3" fill="none"/></g>' % c
    f = '''<rect x="322" y="330" width="16" height="430" rx="8" fill="#FFFFFF"/><rect x="322" y="330" width="16" height="430" rx="8" fill="%(INK)s" opacity=".08"/>
<g class="blades" style="transform-origin:330px 330px"><g transform="translate(330 330)">%(bl)s</g></g><circle cx="330" cy="330" r="14" fill="%(ACC)s"/>
<g transform="translate(1140 190)"><g class="co2"><circle r="30" fill="#B9B3AB"/><circle cx="26" cy="-10" r="22" fill="#B9B3AB"/></g><g class="co2"><circle cx="30" cy="20" r="26" fill="#C8C2BA"/></g></g>
%(l1)s%(l2)s%(l3)s%(l4)s
<g class="heart"><path d="M1105 460 C1040 410 1060 360 1105 392 C1150 360 1170 410 1105 460z" fill="%(ACC)s"/></g>
%(sh)s%(r)s''' % dict(INK=INK, ACC=ACCENT, bl=''.join('<path d="M0 0 L-12 -150 Q0 -170 12 -150 Z" fill="#FFFFFF" transform="rotate(%d)"/>' % a for a in (0, 120, 240)),
                      l1=leaf(TEAL), l2=leaf('#6DB38F'), l3=leaf(MUSTARD), l4=leaf('#3E8C72'), sh=shadow(790), r=place(kick(shirt='#E9742B', helmet='#6DB38F', scarf=MUSTARD), 800, 1.05))
    return scene('ecologie', 'Illustration animée : une éolienne tourne, des feuilles s’envolent et une personne roule en trottinette électrique dans une ville verte',
                 13, css, f, sky=('#FFE3C8', '#FFF0DC', '#FFF7EC'), tree_cols=(TEAL, '#3E8C72', '#2F8F5C', TEAL_D), sun_pos=(1250, 220))


def s_scooter45():
    css = '''
.needle{transform-origin:330px 420px;animation:needle 5s ease-in-out infinite}
@keyframes needle{0%{transform:rotate(-115deg)}45%,60%{transform:rotate(25deg)}100%{transform:rotate(-115deg)}}
.rider{animation:bob .35s ease-in-out infinite}
.speed2 line{animation:speed .6s linear infinite}.speed2 line:nth-child(2){animation-delay:-.2s}.speed2 line:nth-child(3){animation-delay:-.4s}.speed2 line:nth-child(4){animation-delay:-.1s}
.wheel{animation:spin .25s linear infinite}
'''
    ticks = ''.join('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%d" stroke-linecap="round"/>'
                    % (330 + 150 * math.cos(math.radians(a)), 420 + 150 * math.sin(math.radians(a)), 330 + (126 if i % 3 == 0 else 136) * math.cos(math.radians(a)),
                       420 + (126 if i % 3 == 0 else 136) * math.sin(math.radians(a)), INK, 6 if i % 3 == 0 else 3) for i, a in enumerate(range(-205, 26, 21)))
    f = '''<g><circle cx="330" cy="420" r="190" fill="#FFFFFF"/><circle cx="330" cy="420" r="190" fill="none" stroke="%(INK)s" stroke-width="12"/>
<path d="M174 430 A 156 156 0 0 1 330 264" fill="none" stroke="#2F9E6B" stroke-width="16" stroke-linecap="round" opacity=".85"/><path d="M330 264 A 156 156 0 0 1 486 430" fill="none" stroke="%(ACC)s" stroke-width="16" stroke-linecap="round" opacity=".9"/>
%(ticks)s<g class="needle"><path d="M330 420 L330 300 L322 420 Z" fill="%(ACC)s"/><path d="M330 420 L330 300 L338 420 Z" fill="#C93E0C"/></g><circle cx="330" cy="420" r="20" fill="%(INK)s"/>
%(t45)s%(kmh)s</g>
<g class="speed2" stroke="#FFE6DA" stroke-width="8" stroke-linecap="round"><line x1="420" y1="690" x2="520" y2="690"/><line x1="380" y1="760" x2="500" y2="760"/><line x1="440" y1="830" x2="540" y2="830"/><line x1="360" y1="900" x2="470" y2="900"/></g>
%(sh)s%(r)s''' % dict(INK=INK, ACC=ACCENT, ticks=ticks, t45=txt(330, 506, '45', 54, INK, 800), kmh=txt(330, 542, 'km/h', 24, '#7A7E78', 700),
                      sh=shadow(1010, 230), r=place(moped(), 1010, 1.0))
    return scene('scooter-45', 'Illustration animée : un compteur de vitesse monte jusqu’à 45 km/h pendant qu’une personne file sur un scooter électrique',
                 14, css, f, '.needle{transform:rotate(25deg)}', sky=('#FFC9A8', '#FFE3CF', '#FFF2E6'), sun_pos=(1300, 200), mid_cols=(CORAL, ACCENT, '#E8693A', '#3A3D3A'))


def s_volee():
    css = '''
.shackle{animation:shackle 4s ease-in-out infinite}
@keyframes shackle{0%,10%{transform:translateY(-34px)}35%,85%{transform:translateY(0)}100%{transform:translateY(-34px)}}
.lockbody{animation:lockb 4s ease-in-out infinite;transform-origin:330px 380px}
@keyframes lockb{35%{transform:scale(1.04)}42%{transform:scale(1)}}
.key{transform-origin:640px 520px;animation:key 3s ease-in-out infinite alternate}
@keyframes key{from{transform:rotate(-10deg)}to{transform:rotate(10deg)}}
.twinkle{animation:spark 2.2s ease-in-out infinite}.twinkle:nth-of-type(2){animation-delay:-.7s}.twinkle:nth-of-type(3){animation-delay:-1.4s}
@keyframes spark{0%,100%{opacity:0;transform:scale(.4)}50%{opacity:1;transform:scale(1)}}
'''
    star = lambda x, y, d: '<g class="twinkle" style="transform-origin:%dpx %dpx;animation-delay:%ss"><path d="M%d %d l7 -20 l7 20 l20 7 l-20 7 l-7 20 l-7 -20 l-20 -7z" fill="#FFC23D"/></g>' % (x, y, d, x - 7, y - 7)
    chain = ''.join('<ellipse cx="%d" cy="%d" rx="20" ry="11" fill="none" stroke="#7A8084" stroke-width="8" transform="rotate(%d %d %d)"/>' % (x, y, a, x, y) for x, y, a in
                    [(1010, 800, 20), (1038, 818, -30), (1062, 840, 30), (1082, 866, -20), (1100, 890, 40)])
    f = '''<g class="float"><g class="lockbody"><path class="shackle" d="M262 380 V300 Q262 232 330 232 Q398 232 398 300 V380" fill="none" stroke="#9AA0A6" stroke-width="30" stroke-linecap="round"/>
<rect x="222" y="372" width="216" height="170" rx="30" fill="%(ACC)s"/><rect x="222" y="372" width="216" height="64" rx="30" fill="#FF7A45" opacity=".55"/>
<circle cx="330" cy="448" r="24" fill="%(INK)s"/><rect x="321" y="450" width="18" height="52" rx="8" fill="%(INK)s"/></g></g>
<g class="key"><circle cx="640" cy="520" r="30" fill="none" stroke="#E8A21F" stroke-width="13"/><rect x="662" y="514" width="104" height="13" rx="6" fill="#E8A21F"/><rect x="738" y="526" width="13" height="26" rx="5" fill="#E8A21F"/><rect x="714" y="526" width="13" height="18" rx="5" fill="#E8A21F"/></g>
%(s1)s%(s2)s%(s3)s
<rect x="1070" y="470" width="20" height="360" rx="8" fill="#7A8084"/><rect x="1056" y="460" width="48" height="20" rx="10" fill="#9AA0A6"/>
<path d="M1010 784 Q1070 790 1100 884" fill="none" stroke="#7A8084" stroke-width="3" opacity="0"/>%(chain)s
<g transform="translate(1040 810)"><rect x="-17" y="-14" width="34" height="34" rx="8" fill="%(ACC)s"/><path d="M-9 -14 v-9 a9 9 0 0 1 18 0 v9" fill="none" stroke="#9AA0A6" stroke-width="6"/></g>
%(sh)s%(r)s''' % dict(ACC=ACCENT, INK=INK, s1=star(500, 300, 0), s2=star(150, 520, .7), s3=star(560, 640, 1.4), chain=chain, sh=shadow(850, 170),
                      r=place(kick(rider=False), 850, 1.0).replace('class="rider"', 'class="rider" style="animation:none"').replace('class="wheel"', 'class=""'))
    return scene('volee', 'Illustration animée : un gros cadenas se referme, une clé se balance et une trottinette électrique est attachée à un poteau en pleine rue',
                 15, css, f, '.shackle{transform:none}', road_scroll=False, sun_pos=(1300, 190))


def s_pluie():
    css = '''
.rain line{stroke:#6FA6C8;stroke-width:4;stroke-linecap:round;animation:rain .8s linear infinite}
@keyframes rain{from{transform:translate(0,-60px)}to{transform:translate(-50px,900px)}}
.puddle{transform-box:fill-box;transform-origin:center;animation:rip 2.4s ease-out infinite;opacity:0}
.puddle:nth-of-type(2){animation-delay:-.8s}.puddle:nth-of-type(3){animation-delay:-1.6s}
@keyframes rip{0%{opacity:.9;transform:scale(.2)}100%{opacity:0;transform:scale(1.5)}}
.rainbow{animation:rb 6s ease-in-out infinite}
@keyframes rb{0%,100%{opacity:.35}50%{opacity:.95}}
.sunpeek{animation:sunpeek 6s ease-in-out infinite}
@keyframes sunpeek{50%{transform:translate(20px,-10px)}}
'''
    rnd = random.Random(5)
    rain = ''.join('<line x1="%d" y1="0" x2="%d" y2="34" style="animation-delay:-%.2fs;animation-duration:%.2fs"/>' % (x, x - 12, rnd.random() * .8, .7 + rnd.random() * .3) for x in range(0, 1700, 46))
    arcs = ''.join('<path d="M%d 560 A %d %d 0 0 1 %d 560" fill="none" stroke="%s" stroke-width="22"/>' % (1090 - r, r, r, 1090 + r, c)
                   for r, c in [(330, '#FF5A5A'), (306, '#FFA94D'), (282, '#FFD84D'), (258, '#7BD389'), (234, '#5AB8E8'), (210, '#9B7BE0')])
    f = '''<g class="rainbow">%(arcs)s</g>
<g class="sunpeek"><circle cx="1290" cy="230" r="96" fill="%(SUN)s"/><circle cx="1290" cy="230" r="70" fill="#FFC769"/></g>
<g class="clouds2"><g class="float">%(c1)s</g><g class="float" style="animation-delay:-2s">%(c2)s</g></g>
<g class="rain">%(rain)s</g>
<ellipse class="puddle" cx="400" cy="920" rx="150" ry="22" fill="none" stroke="#9CC6E0" stroke-width="5"/><ellipse class="puddle" cx="1150" cy="960" rx="150" ry="22" fill="none" stroke="#9CC6E0" stroke-width="5"/><ellipse class="puddle" cx="760" cy="975" rx="150" ry="22" fill="none" stroke="#9CC6E0" stroke-width="5"/>
%(sh)s%(r)s''' % dict(arcs=arcs, SUN=SUN, c1=cloud(300, 170, 1.7, '#C9D3DC'), c2=cloud(820, 130, 1.4, '#D6DEE5'), rain=rain, sh=shadow(760),
                      r=place(kick(shirt='#FFC21F', shirt_d='#E0A010', helmet='#FFC21F', pants='#2B3A5A', scarf='#FFC21F', bag='#2B3A5A'), 760, 1.05))
    return scene('pluie', 'Illustration animée : sous une pluie qui tombe, une personne en ciré jaune roule en trottinette électrique, un arc-en-ciel apparaît derrière elle',
                 16, css, f, '.rain{display:none}.puddle{opacity:.6}', sky=('#C9DCE8', '#E4EBEE', '#FBEFE6'), show_sun=False, cloud_fill='#D8E1E8',
                 back_cols=('#E3B9A6', '#D8B3A4', '#EBC8B8'), mid_cols=('#D88A6A', '#E0714A', '#C7623D', '#3A3D3A'))


def s_choisir():
    css = '''
.arrowL{transform-origin:768px 420px;animation:arL 3s ease-in-out infinite alternate}.arrowR{transform-origin:768px 420px;animation:arR 3s ease-in-out infinite alternate}
@keyframes arL{to{transform:rotate(-3deg)}}@keyframes arR{to{transform:rotate(3deg)}}
.qm{animation:float 2.6s ease-in-out infinite}
.rider{animation:bob .9s ease-in-out infinite}
'''
    f = '''<rect x="756" y="300" width="26" height="540" rx="10" fill="#7A8084"/>
<g class="arrowL"><path d="M768 286 H506 L440 340 L506 394 H768 Z" fill="%(TEAL)s"/>%(t1)s</g>
<g class="arrowR"><path d="M768 400 H1030 L1096 454 L1030 508 H768 Z" fill="%(ACC)s"/>%(t2)s</g>
<g class="qm"><circle cx="768" cy="190" r="56" fill="%(MU)s"/>%(q)s</g>
%(sh1)s%(sh2)s%(a)s%(b)s''' % dict(TEAL=TEAL, ACC=ACCENT, MU=MUSTARD, t1=txt(640, 356, 'Trottinette', 36), t2=txt(902, 470, 'Scooter', 36),
                                   q=txt(768, 220, '?', 80, INK, 800), sh1=shadow(300, 170), sh2=shadow(1240, 200),
                                   a=place(kick(), 300, .8), b=place(moped(), 1240, .85))
    return scene('choisir', 'Illustration animée : un panneau à deux flèches propose une trottinette d’un côté et un scooter électrique de l’autre, un point d’interrogation flotte au-dessus',
                 17, css, f, sun_pos=(1330, 160), road_scroll=False)


def s_batterie():
    css = '''
.fill{transform-box:fill-box;transform-origin:left center;animation:fill 6s ease-in-out infinite}
@keyframes fill{0%{transform:scaleX(.12)}70%,90%{transform:scaleX(1)}100%{transform:scaleX(.12)}}
.bolt{transform-origin:768px 330px;animation:bolt 1.6s ease-in-out infinite}
@keyframes bolt{50%{transform:scale(1.14) rotate(-4deg)}}
.cable{transform-origin:380px 330px;animation:sway 3s ease-in-out infinite alternate}
.pct{animation:pct 6s steps(1) infinite}
.cell{animation:cell 6s ease-in-out infinite;opacity:.25}.cell:nth-of-type(2){animation-delay:.5s}.cell:nth-of-type(3){animation-delay:1s}.cell:nth-of-type(4){animation-delay:1.5s}.cell:nth-of-type(5){animation-delay:2s}
@keyframes cell{15%,85%{opacity:1}100%{opacity:.25}}
.sparkle{animation:spark 2.4s ease-in-out infinite}.sparkle:nth-of-type(2){animation-delay:-.8s}
@keyframes spark{0%,100%{opacity:0;transform:scale(.4)}50%{opacity:1;transform:scale(1)}}
'''
    cells = ''.join('<rect class="cell" x="%d" y="266" width="86" height="130" rx="12" fill="#FFFFFF"/>' % (520 + i * 100) for i in range(5))
    f = '''<g class="cable"><path d="M384 330 C300 330 300 230 210 230" fill="none" stroke="%(INK)s" stroke-width="12" stroke-linecap="round"/><rect x="150" y="204" width="64" height="52" rx="12" fill="%(INK)s"/><rect x="128" y="216" width="30" height="8" rx="4" fill="#7A8084"/><rect x="128" y="236" width="30" height="8" rx="4" fill="#7A8084"/></g>
<rect x="380" y="206" width="780" height="248" rx="44" fill="%(INK)s"/><rect x="1160" y="278" width="50" height="104" rx="18" fill="%(INK)s"/>
<rect x="404" y="230" width="732" height="200" rx="28" fill="#FFF4EA"/>
<rect class="fill" x="410" y="236" width="720" height="188" rx="24" fill="#3AAA6E"/>
<g>%(cells)s</g>
<g class="bolt"><path d="M790 250 L714 350 H764 L744 420 L828 304 H776 Z" fill="#FFC23D" stroke="#E8941C" stroke-width="6" stroke-linejoin="round"/></g>
<g class="sparkle" style="transform-origin:1190px 200px"><path d="M1190 170 l8 22 l22 8 l-22 8 l-8 22 l-8 -22 l-22 -8 l22 -8z" fill="#FFC23D"/></g>
<g class="sparkle" style="transform-origin:340px 440px"><path d="M340 410 l7 20 l20 7 l-20 7 l-7 20 l-7 -20 l-20 -7 l20 -7z" fill="#FFC23D"/></g>
%(sh)s%(r)s''' % dict(INK=INK, cells=cells, sh=shadow(780, 200), r=place(kick(shirt='#2F9E6B', shirt_d='#1F7A50', helmet=MUSTARD), 780, 1.0))
    return scene('batterie', 'Illustration animée : une batterie se recharge, un éclair pulse, et une personne roule en trottinette électrique en dessous',
                 18, css, f, '.fill{transform:none}.cell{opacity:1}', sun_pos=(1330, 170), cloud_pts=[(200, 560, .8), (1100, 600, .7), (700, 580, .6)])


def s_smart_ultra():
    css = '''
.vs{transform-origin:768px 330px;animation:vs 2.4s ease-in-out infinite}
@keyframes vs{50%{transform:scale(1.12) rotate(-3deg)}}
.ringL{transform-origin:360px 570px;animation:ring 4s ease-in-out infinite}
.ringR{transform-origin:1176px 570px;animation:ring 4s ease-in-out infinite;animation-delay:-2s}
@keyframes ring{0%,100%{opacity:.15;transform:scale(.92)}50%{opacity:.7;transform:scale(1.05)}}
.rider{animation:bob .9s ease-in-out infinite}.r2 .rider{animation-delay:-.45s}
'''
    f = '''<circle class="ringL" cx="360" cy="570" r="250" fill="none" stroke="%(TEAL)s" stroke-width="12" stroke-dasharray="26 18"/>
<circle class="ringR" cx="1176" cy="570" r="250" fill="none" stroke="%(ACC)s" stroke-width="12" stroke-dasharray="26 18"/>
<g class="vs"><circle cx="768" cy="330" r="82" fill="%(INK)s"/>%(vs)s</g>
%(sh1)s%(sh2)s%(a)s<g class="r2">%(b)s</g>''' % dict(TEAL=TEAL, ACC=ACCENT, INK=INK, vs=txt(768, 354, 'VS', 64, '#FFFFFF', 800), sh1=shadow(360, 170), sh2=shadow(1176, 190),
                                                   a=place(kick(shirt=TEAL, helmet=MUSTARD), 360, .9), b=place(kick(shirt=NAVY, shirt_d='#16213A', helmet=ACCENT, pants='#3A3D3A', scarf=MUSTARD, bag='#C93E0C'), 1176, 1.04))
    return scene('smart-ultra', 'Illustration animée : deux personnes sur deux trottinettes électriques se font face, un badge VS pulse entre elles',
                 19, css, f, sun_pos=(1330, 160), road_scroll=False)


def s_train():
    css = '''
.train{animation:train 14s linear infinite}
@keyframes train{from{transform:translateX(-1900px)}to{transform:translateX(1700px)}}
.winb{animation:glow 1.2s ease-in-out infinite alternate}
@keyframes glow{to{opacity:.75}}
.puff{animation:puff 3s ease-out infinite;opacity:0;transform-origin:center;transform-box:fill-box}.puff:nth-of-type(2){animation-delay:-1s}.puff:nth-of-type(3){animation-delay:-2s}
@keyframes puff{0%{opacity:.8;transform:translate(0,0) scale(.4)}100%{opacity:0;transform:translate(-60px,-100px) scale(1.3)}}
.tag{transform-origin:900px 640px;animation:sway 2.6s ease-in-out infinite alternate}
'''
    car = lambda x, col: ('<g transform="translate(%d 0)"><rect x="0" y="470" width="560" height="260" rx="40" fill="%s"/><rect x="0" y="650" width="560" height="26" fill="%s" opacity=".5"/>'
                         '%s<rect x="20" y="722" width="520" height="22" rx="8" fill="%s"/><circle cx="90" cy="750" r="30" fill="#121412"/><circle cx="470" cy="750" r="30" fill="#121412"/></g>') % (
        x, col, INK, ''.join('<rect class="winb" x="%d" y="510" width="96" height="120" rx="18" fill="#FFF1DE"/>' % (x2) for x2 in range(40, 540, 126)), INK)
    wheels_pairs = ''
    tr = '<g class="train">' + car(0, ACCENT) + car(580, '#E9742B') + car(1160, ACCENT) + '</g>'
    f = '''<rect y="760" width="1536" height="30" fill="#F2C6A8"/><rect y="790" width="1536" height="36" fill="#E3A982"/>
%(tr)s
<rect y="800" width="1536" height="224" fill="%(INK)s"/><rect y="800" width="1536" height="14" fill="#F2C94C"/>
<rect x="150" y="440" width="12" height="360" rx="5" fill="#7A8084"/><rect x="104" y="420" width="104" height="52" rx="10" fill="#2F7A6B"/>%(tg)s
<g class="float" style="animation-delay:-1s"><g class="tag"><rect x="860" y="560" width="120" height="70" rx="12" fill="#FFFFFF"/><rect x="860" y="560" width="120" height="22" rx="12" fill="%(ACC)s"/>%(ok)s</g></g>
%(sh)s%(w)s%(fold)s''' % dict(
        tr=tr, INK=INK, ACC=ACCENT, tg=txt(156, 456, 'GARE', 24, '#FFFFFF', 700), ok='<path d="M894 606 l14 14 l30 -34" fill="none" stroke="#1F9E5B" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>',
        sh=shadow(700, 130), w=place(standing(shirt=TEAL, pants=NAVY, hair='#3B2416'), 700),
        fold='''<g transform="translate(790 0)" class="float"><g transform="translate(40 0)">
 <rect x="0" y="880" width="170" height="18" rx="9" fill="#121412"/><line x1="160" y1="882" x2="170" y2="716" stroke="#121412" stroke-width="16" stroke-linecap="round" transform="rotate(-80 160 882)"/>
 <line x1="170" y1="800" x2="186" y2="806" stroke="#121412" stroke-width="12" stroke-linecap="round"/>
 <circle cx="28" cy="906" r="34" fill="#121412"/><circle cx="28" cy="906" r="23" fill="#3A3D3A"/><circle cx="28" cy="906" r="6" fill="%s"/>
 <circle cx="150" cy="906" r="34" fill="#121412"/><circle cx="150" cy="906" r="23" fill="#3A3D3A"/><circle cx="150" cy="906" r="6" fill="%s"/>
 <rect x="86" y="858" width="26" height="22" rx="6" fill="%s"/></g></g>''' % (ACCENT, ACCENT, MUSTARD))
    return scene('train', 'Illustration animée : un train traverse la gare pendant qu’un voyageur attend sur le quai avec sa trottinette électrique pliée',
                 20, css, f, '.train{transform:translateX(200px)}', road_scroll=False, sun_pos=(1330, 170))


def s_avis():
    css = '''
.star{transform-box:fill-box;transform-origin:center;animation:star 3.5s ease-in-out infinite;opacity:.25}
.star:nth-of-type(2){animation-delay:.25s}.star:nth-of-type(3){animation-delay:.5s}.star:nth-of-type(4){animation-delay:.75s}.star:nth-of-type(5){animation-delay:1s}
@keyframes star{0%,10%{opacity:.25;transform:scale(.8)}25%,85%{opacity:1;transform:scale(1)}100%{opacity:.25;transform:scale(.8)}}
.bub{animation:float 4s ease-in-out infinite}.bub2{animation:float 4.6s ease-in-out infinite;animation-delay:-1.5s}
.wrench{transform-origin:1180px 470px;animation:wrench 2.2s ease-in-out infinite}
@keyframes wrench{0%,100%{transform:rotate(-18deg)}50%{transform:rotate(18deg)}}
.heart{transform-origin:1000px 250px;animation:pulse 1.6s ease-in-out infinite}
'''
    star = lambda x, y: ('<g class="star"><path d="M%d %d l17 35 l38 5 l-28 26 l7 38 l-34 -18 l-34 18 l7 -38 l-28 -26 l38 -5z" fill="#FFC23D" stroke="#E8941C" stroke-width="5" stroke-linejoin="round"/></g>' % (x, y))
    f = '''<g class="bub"><rect x="210" y="130" width="560" height="180" rx="40" fill="#FFFFFF"/><path d="M330 306 l-10 60 l60 -58z" fill="#FFFFFF"/>
%(stars)s</g>
<g class="bub2"><rect x="880" y="170" width="250" height="150" rx="34" fill="%(TEAL)s"/><path d="M960 316 l-6 46 l46 -44z" fill="%(TEAL)s"/>
<rect x="912" y="208" width="150" height="14" rx="7" fill="#FFFFFF" opacity=".85"/><rect x="912" y="238" width="186" height="14" rx="7" fill="#FFFFFF" opacity=".6"/><rect x="912" y="268" width="120" height="14" rx="7" fill="#FFFFFF" opacity=".6"/></g>
<g class="heart"><path d="M1000 282 C952 246 966 208 1000 232 C1034 208 1048 246 1000 282z" fill="%(ACC)s"/></g>
<g class="wrench"><rect x="1166" y="440" width="28" height="230" rx="14" fill="#8A9096"/><path d="M1140 452 A52 52 0 0 1 1158 372 L1166 412 L1194 412 L1202 372 A52 52 0 0 1 1220 452 Q1180 478 1140 452 Z" fill="#9AA0A6"/><circle cx="1180" cy="640" r="9" fill="#6E747A"/></g>
%(sh)s%(r)s''' % dict(stars=''.join(star(250 + i * 104, 165) for i in range(5)), TEAL=TEAL, ACC=ACCENT, sh=shadow(620), r=place(kick(shirt='#E9742B', helmet=TEAL, scarf=MUSTARD), 620, 1.0))
    return scene('avis', 'Illustration animée : des étoiles de notation et des bulles d’avis flottent au-dessus d’une personne qui roule en trottinette électrique, une clé de réparation tourne à côté',
                 21, css, f, '.star{opacity:1}', sun_pos=(1360, 140), cloud_pts=[(180, 560, .7), (900, 600, .6)])


def s_financement():
    css = '''
.page{transform-origin:330px 200px;animation:flip 3s ease-in-out infinite}
@keyframes flip{0%,30%{transform:scaleY(1)}50%{transform:scaleY(-.05)}51%,100%{transform:scaleY(0);opacity:0}}
.coin{animation:drop 2.4s ease-in infinite;opacity:0}.coin:nth-of-type(2){animation-delay:.8s}.coin:nth-of-type(3){animation-delay:1.6s}
@keyframes drop{0%{opacity:0;transform:translateY(-120px)}15%{opacity:1}80%{opacity:1;transform:translateY(120px)}100%{opacity:0;transform:translateY(140px)}}
.pig{transform-origin:1040px 470px;animation:pig 2.4s ease-in-out infinite}
@keyframes pig{0%,70%,100%{transform:scale(1)}80%{transform:scale(1.05,0.96)}}
.card{animation:card 5s ease-in-out infinite;transform-origin:700px 330px}
@keyframes card{0%,100%{transform:translateY(0) rotate(-8deg)}50%{transform:translateY(-16px) rotate(-3deg)}}
'''
    days = ''.join('<rect x="%d" y="%d" width="34" height="26" rx="6" fill="%s"/>' % (232 + (i % 5) * 42, 250 + (i // 5) * 36, ACCENT if i == 7 else '#EDE6DC') for i in range(15))
    coin = lambda x, d: ('<g class="coin" style="animation-delay:%ss"><circle cx="%d" cy="300" r="26" fill="#FFC23D" stroke="#E8941C" stroke-width="5"/>%s</g>' % (d, x, txt(x, 311, '€', 30, '#A85A0A')))
    f = '''<g><rect x="210" y="160" width="240" height="250" rx="26" fill="#FFFFFF"/><rect x="210" y="160" width="240" height="70" rx="26" fill="%(TEAL)s"/><rect x="210" y="200" width="240" height="30" fill="%(TEAL)s"/>
<rect x="250" y="140" width="16" height="44" rx="8" fill="%(INK)s"/><rect x="394" y="140" width="16" height="44" rx="8" fill="%(INK)s"/>%(days)s</g>
<g class="page"><rect x="210" y="160" width="240" height="70" rx="26" fill="#3E8C72"/>%(m)s</g>
<g class="card"><rect x="580" y="260" width="250" height="150" rx="20" fill="%(ACC)s"/><rect x="580" y="296" width="250" height="30" fill="%(INK)s" opacity=".8"/><rect x="606" y="350" width="60" height="38" rx="8" fill="#FFC23D"/><rect x="690" y="362" width="110" height="12" rx="6" fill="#FFFFFF" opacity=".7"/></g>
%(c1)s%(c2)s%(c3)s
<g class="pig"><ellipse cx="1040" cy="480" rx="150" ry="110" fill="#FF9BB0"/><circle cx="1170" cy="460" r="46" fill="#FF9BB0"/><ellipse cx="1196" cy="466" rx="22" ry="18" fill="#FF7A98"/>
<circle cx="1150" cy="438" r="7" fill="%(INK)s"/><path d="M1000 380 l30 -36 l24 40z" fill="#FF7A98"/><rect x="990" y="376" width="90" height="14" rx="7" fill="#C2475F"/>
<rect x="940" y="570" width="34" height="50" rx="12" fill="#FF7A98"/><rect x="1090" y="570" width="34" height="50" rx="12" fill="#FF7A98"/></g>
%(sh)s%(r)s''' % dict(TEAL=TEAL, INK=INK, ACC=ACCENT, days=days, m=txt(330, 210, '12 · 24 · 36', 28, '#FFFFFF', 800),
                      c1=coin(1010, 0), c2=coin(1050, .8), c3=coin(1090, 1.6), sh=shadow(560, 180), r=place(kick(shirt=NAVY, helmet=MUSTARD, scarf=ACCENT), 560, .95))
    return scene('financement', 'Illustration animée : les pages d’un calendrier tournent, des pièces en euros tombent dans une tirelire et une carte bancaire flotte au-dessus d’une personne en trottinette électrique',
                 22, css, f, '.coin{opacity:1}', sun_pos=(1360, 140), cloud_pts=[(160, 580, .7), (1300, 600, .6)])


SCENES = {'avis': s_avis, 'financement': s_financement, 'louer-acheter': s_louer_acheter, 'assurance': s_assurance, 'ecologie': s_ecologie, 'scooter-45': s_scooter45, 'volee': s_volee,
          'pluie': s_pluie, 'choisir': s_choisir, 'batterie': s_batterie, 'smart-ultra': s_smart_ultra, 'train': s_train}

if __name__ == '__main__':
    ids = sys.argv[1:] or list(SCENES)
    os.makedirs(OUT, exist_ok=True)
    for i in ids:
        svg = SCENES[i]()
        open(OUT + 'anim-%s.svg' % i, 'w', encoding='utf-8', newline='\n').write(svg)
        print('img/conseils/anim-%s.svg' % i, len(svg) // 1024, 'Ko')
