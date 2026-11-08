# -*- coding: utf-8 -*-
"""Illustration animée (SVG + CSS, sans JavaScript) de l'article « forfait mobilités durables ».
    python tools/illustration_fmd.py   ->  img/conseils/anim-fmd.svg
Couleurs reprises de css/style.css (accent #FF5A1F, crème, encre) avec des tons chauds en plus.
Les animations s'arrêtent si le visiteur a demandé moins d'animations (prefers-reduced-motion)."""
import os, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
W, H = 1536, 1024
rnd = random.Random(7)

ACCENT, INK, CREAM = '#FF5A1F', '#2B2E2B', '#FFF4EA'
SUN, SUN_D = '#FFB547', '#FF9F2E'
PEACH, CORAL = '#FFC7A6', '#FF9466'
TEAL, TEAL_D = '#2F7A6B', '#22594E'
MUSTARD, NAVY, SKIN = '#F2A93B', '#23304A', '#A8673F'


def skyline(base, hmin, hmax, wmin, wmax, colors, win, gap=6, round_top=False):
    """Une rangée d'immeubles de 0 à W, répétée une fois à droite pour boucler sans couture."""
    out, x = [], 0
    while x < W:
        w = rnd.randint(wmin, wmax)
        w = min(w, W - x) if W - x < wmin + 20 else w
        h = rnd.randint(hmin, hmax)
        c = rnd.choice(colors)
        r = 14 if round_top else 6
        out.append('<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s"/>' % (x, base - h, w, h + 40, r, c))
        if win:
            for wy in range(base - h + 26, base - 30, 38):
                for wx in range(x + 16, x + w - 24, 30):
                    if rnd.random() < .78:
                        out.append('<rect x="%d" y="%d" width="12" height="18" rx="3" fill="%s"/>' % (wx, wy, win))
        x += w + gap
    g = ''.join(out)
    return '<g>%s</g><g transform="translate(%d 0)">%s</g>' % (g, W, g)


def trees(base):
    out, x = [], 40
    while x < W - 40:
        h = rnd.randint(90, 130)
        r = rnd.randint(46, 62)
        c = rnd.choice([TEAL, '#3E8C72', TEAL_D])
        out.append('<rect x="%d" y="%d" width="10" height="%d" rx="4" fill="#7A4A2B"/>' % (x - 5, base - h + r, h - r))
        out.append('<g class="sway" style="animation-delay:-%.1fs"><circle cx="%d" cy="%d" r="%d" fill="%s"/><circle cx="%d" cy="%d" r="%d" fill="%s" opacity=".55"/></g>'
                   % (rnd.random() * 3, x, base - h, r, c, x - r * .35, base - h - r * .3, r * .45, '#5FA88A'))
        x += rnd.randint(240, 330)
    g = ''.join(out)
    return '<g>%s</g><g transform="translate(%d 0)">%s</g>' % (g, W, g)


def cloud(x, y, s):
    return ('<g transform="translate(%d %d) scale(%.2f)"><ellipse cx="0" cy="0" rx="70" ry="30" fill="%s"/>'
            '<circle cx="-28" cy="-18" r="32" fill="%s"/><circle cx="22" cy="-26" r="40" fill="%s"/></g>') % (x, y, s, CREAM, CREAM, CREAM)


def wheel(cx, cy):
    spokes = ''.join('<line x1="0" y1="0" x2="%.1f" y2="%.1f" stroke="#8A8D86" stroke-width="4" stroke-linecap="round"/>'
                     % (24 * __import__('math').cos(a * 1.0472), 24 * __import__('math').sin(a * 1.0472)) for a in range(6))
    return ('<g transform="translate(%d %d)"><g class="wheel"><circle r="42" fill="#121412"/><circle r="30" fill="#3A3D3A"/>%s'
            '<circle r="8" fill="%s"/></g></g>') % (cx, cy, spokes, ACCENT)


rays = ''.join('<rect x="-7" y="-196" width="14" height="44" rx="7" fill="%s" transform="rotate(%d)"/>' % (SUN, a) for a in range(0, 360, 30))

coins = ''
for i, (dx, delay) in enumerate([(-60, 0), (40, 1.1), (-10, 2.2), (90, 3.3), (-110, 4.4)]):
    coins += ('<g class="coin c%d" style="animation-delay:%.1fs"><circle r="27" fill="#FFC23D" stroke="#E8941C" stroke-width="5"/>'
              '<text y="11" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="32" fill="#A85A0A">€</text></g>') % (i % 3, delay)

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %(W)d %(H)d" width="%(W)d" height="%(H)d" role="img" aria-labelledby="t">
<title id="t">Illustration : un salarié file en trottinette électrique dans une ville ensoleillée, des pièces en euros s'envolent derrière lui</title>
<style>
.scroll-slow{animation:scroll 70s linear infinite}
.scroll-mid{animation:scroll 26s linear infinite}
.scroll-fast{animation:scroll 11s linear infinite}
.clouds{animation:scroll 120s linear infinite}
@keyframes scroll{to{transform:translateX(-%(W)dpx)}}
.rays{transform-origin:0 0;animation:spin 40s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.sun-core{transform-origin:1190px 250px;animation:pulse 4s ease-in-out infinite}
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
.coin{opacity:0;transform:translate(700px,600px);animation:rise0 5.5s ease-out infinite}
.coin.c1{animation-name:rise1}.coin.c2{animation-name:rise2}
@keyframes rise0{0%%{opacity:0;transform:translate(705px,600px) scale(.5)}12%%{opacity:1}80%%{opacity:1}100%%{opacity:0;transform:translate(560px,250px) scale(1.05) rotate(-20deg)}}
@keyframes rise1{0%%{opacity:0;transform:translate(705px,600px) scale(.5)}12%%{opacity:1}80%%{opacity:1}100%%{opacity:0;transform:translate(660px,190px) scale(1.1) rotate(15deg)}}
@keyframes rise2{0%%{opacity:0;transform:translate(705px,600px) scale(.5)}12%%{opacity:1}80%%{opacity:1}100%%{opacity:0;transform:translate(460px,300px) scale(.95) rotate(-35deg)}}
.badge{transform-origin:330px 250px;animation:badge 5.5s ease-in-out infinite}
@keyframes badge{0%%,100%%{transform:translateY(0) rotate(-4deg)}50%%{transform:translateY(-12px) rotate(-1deg)}}
.bird{animation:bird 30s linear infinite}
@keyframes bird{from{transform:translate(1600px,0)}to{transform:translate(-200px,-60px)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.coin{opacity:1}.coin.c0{transform:translate(610px,380px)}.coin.c1{transform:translate(680px,300px)}.coin.c2{transform:translate(540px,430px)}}
</style>
<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD7BE"/><stop offset=".65" stop-color="#FFEBDC"/><stop offset="1" stop-color="#FFF4EA"/></linearGradient>
</defs>
<rect width="%(W)d" height="%(H)d" fill="url(#sky)"/>
<g transform="translate(1190 250)"><g class="rays">%(rays)s</g></g>
<circle class="sun-core" cx="1190" cy="250" r="130" fill="%(SUN)s"/>
<circle cx="1190" cy="250" r="96" fill="#FFC769"/>
<g class="clouds">%(clouds)s</g>
<g class="bird"><path d="M0 120 q14 -14 28 0 q14 -14 28 0" fill="none" stroke="%(INK)s" stroke-width="5" stroke-linecap="round"/><path d="M70 150 q10 -10 20 0 q10 -10 20 0" fill="none" stroke="%(INK)s" stroke-width="4" stroke-linecap="round"/></g>
<g class="scroll-slow">%(back)s</g>
<g class="scroll-mid">%(mid)s</g>
<rect y="760" width="%(W)d" height="60" fill="#F6CDB4"/>
<rect y="812" width="%(W)d" height="10" fill="#E9B394"/>
<g class="scroll-mid">%(trees)s</g>
<rect y="822" width="%(W)d" height="202" fill="%(INK)s"/>
<rect y="838" width="%(W)d" height="6" fill="%(ACCENT)s"/>
<line class="dash" x1="0" y1="985" x2="%(W)d" y2="985" stroke="#FFE6DA" stroke-width="10" stroke-dasharray="70 50"/>
<g class="badge"><g transform="rotate(-6 330 260)">
 <rect x="214" y="166" width="236" height="196" rx="18" fill="#FFFFFF"/>
 <rect x="214" y="166" width="236" height="46" rx="18" fill="%(ACCENT)s"/><rect x="214" y="194" width="236" height="18" fill="%(ACCENT)s"/>
 <rect x="240" y="234" width="120" height="12" rx="6" fill="#E7E4DC"/><rect x="240" y="262" width="150" height="12" rx="6" fill="#E7E4DC"/><rect x="240" y="290" width="96" height="12" rx="6" fill="#E7E4DC"/>
 <circle cx="404" cy="318" r="30" fill="#FFC23D" stroke="#E8941C" stroke-width="5"/><text x="404" y="330" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="32" fill="#A85A0A">€</text>
 <circle cx="444" cy="174" r="26" fill="#1F6B45"/><path d="M432 174 l9 9 l16 -18" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g></g>
%(coins)s
<g class="speed" stroke="#FFE6DA" stroke-width="7" stroke-linecap="round"><line x1="560" y1="700" x2="620" y2="700"/><line x1="540" y1="760" x2="610" y2="760"/><line x1="580" y1="640" x2="630" y2="640"/></g>
<ellipse cx="760" cy="950" rx="190" ry="14" fill="#121412" opacity=".35"/>
<g class="rider">
 <!-- trottinette -->
 <rect x="618" y="880" width="262" height="20" rx="10" fill="#121412"/>
 <path d="M612 880 q-6 -28 22 -30 h20" fill="none" stroke="#121412" stroke-width="12" stroke-linecap="round"/>
 <line x1="848" y1="612" x2="884" y2="900" stroke="#121412" stroke-width="16" stroke-linecap="round"/>
 <line x1="818" y1="606" x2="886" y2="618" stroke="#121412" stroke-width="12" stroke-linecap="round"/>
 <circle cx="851" cy="622" r="6" fill="%(ACCENT)s"/>
 <circle cx="626" cy="876" r="7" fill="#FF3B2F"/>
 %(w1)s %(w2)s
 <!-- jambes -->
 <path d="M742 700 L712 790 L702 872" fill="none" stroke="%(NAVY)s" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
 <path d="M760 700 L798 784 L792 872" fill="none" stroke="#2E3D5C" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/>
 <path d="M680 868 h44 q8 0 8 10 h-60 q0 -10 8 -10z" fill="#FFFFFF"/><path d="M772 868 h44 q8 0 8 10 h-60 q0 -10 8 -10z" fill="#FFFFFF"/>
 <!-- sac -->
 <rect x="694" y="566" width="62" height="104" rx="22" fill="%(MUSTARD)s" transform="rotate(14 725 618)"/>
 <rect x="704" y="600" width="40" height="30" rx="10" fill="#E0922A" transform="rotate(14 725 618)"/>
 <!-- buste -->
 <path d="M720 712 L788 712 L826 584 Q812 540 768 544 L734 566 Z" fill="%(TEAL)s"/>
 <path d="M770 548 L800 556 L788 712 L760 712 Z" fill="%(TEAL_D)s" opacity=".35"/>
 <!-- bras -->
 <path d="M800 572 L836 612 L850 614" fill="none" stroke="%(TEAL)s" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="852" cy="614" r="13" fill="%(SKIN)s"/>
 <!-- écharpe -->
 <g class="scarf"><path d="M806 548 C770 556 740 552 712 540 L716 560 C744 572 774 574 804 566 Z" fill="%(ACCENT)s"/></g>
 <rect x="784" y="520" width="26" height="34" rx="10" fill="%(SKIN)s"/>
 <!-- tête et casque -->
 <circle cx="800" cy="492" r="38" fill="%(SKIN)s"/>
 <path d="M760 488 a41 41 0 0 1 82 -6 l14 6 q4 4 -2 7 l-94 4 z" fill="%(ACCENT)s"/>
 <path d="M776 470 a30 30 0 0 1 40 -14" fill="none" stroke="#FFB08F" stroke-width="7" stroke-linecap="round"/>
 <circle cx="822" cy="502" r="4.5" fill="#121412"/>
 <path d="M812 520 q10 7 20 0" fill="none" stroke="#121412" stroke-width="4" stroke-linecap="round"/>
 <path d="M770 492 q-8 6 0 14" fill="none" stroke="#8E5232" stroke-width="5" stroke-linecap="round"/>
</g>
</svg>
''' % dict(W=W, H=H, rays=rays, SUN=SUN, INK=INK, ACCENT=ACCENT, NAVY=NAVY, MUSTARD=MUSTARD, TEAL=TEAL, TEAL_D=TEAL_D, SKIN=SKIN,
           clouds=''.join(cloud(x, y, s) for x, y, s in [(180, 120, 1.0), (620, 200, .8), (980, 110, .7), (1400, 180, 1.1)])
                  + '<g transform="translate(%d 0)">' % W + ''.join(cloud(x, y, s) for x, y, s in [(180, 120, 1.0), (620, 200, .8), (980, 110, .7), (1400, 180, 1.1)]) + '</g>',
           back=skyline(760, 220, 400, 110, 190, [PEACH, '#FFBE98', '#FFD0B5'], '#FFE3D2', gap=10, round_top=True),
           mid=skyline(770, 120, 260, 90, 160, [CORAL, ACCENT, '#E8693A', '#3A3D3A'], '#FFE6DA', gap=24),
           trees=trees(800), coins=coins, w1=wheel(640, 905), w2=wheel(880, 905))

os.makedirs(ROOT + 'img/conseils', exist_ok=True)
open(ROOT + 'img/conseils/anim-fmd.svg', 'w', encoding='utf-8', newline='\n').write(svg)
print('img/conseils/anim-fmd.svg', len(svg) // 1024, 'Ko')
