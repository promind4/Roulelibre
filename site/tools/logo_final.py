# -*- coding: utf-8 -*-
"""Logo définitif de Roulelibre (piste D, l'oiseau-roue) : vectorise l'oiseau de l'image Codex et produit tous les fichiers.
    python tools/logo_final.py
Source : tools/logo/codex/d-oiseau-roue.png (moitié gauche : oiseau orange + soleil jaune sur fond crème).
Sorties :
  img/logo-mark.svg            logo du site (sans fond), lisible sur fond crème et sombre
  favicon.svg                  favicon rond (oiseau blanc, soleil jaune, disque orange)
  favicon.ico                  16, 32, 48 px
  favicon-48.png, favicon-192.png, favicon-512.png   (Google : multiples de 48 px)
  apple-touch-icon.png         180 px, carré plein (iOS arrondit les coins)
  img/logo-512.png             logo (sans fond) pour les données structurées et les partages"""
import os, sys
import numpy as np, cv2
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
SRC = ROOT + 'tools/logo/codex/d-oiseau-roue.png'
ORANGE, SUN, INK = (255, 90, 31), (255, 181, 71), (18, 20, 18)
HEX_O, HEX_S = '#FF5A1F', '#FFB547'
K = 4  # sur-échantillonnage pour lisser les contours

im = cv2.cvtColor(cv2.imread(SRC), cv2.COLOR_BGR2RGB).astype(np.float32)
H, W, _ = im.shape
bg = np.median(im[:40, :40].reshape(-1, 3), axis=0)
left = im[:, :W // 2]

# ---- soleil : plus grande zone jaune de la moitié gauche
d_y = np.linalg.norm(left - np.array(SUN), axis=2)
yel = (d_y < 28).astype(np.uint8)
n, lab, st, cen = cv2.connectedComponentsWithStats(yel)
k = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
ys, xs = np.where(lab == k)
(sx, sy), sr = cv2.minEnclosingCircle(np.stack([xs, ys], 1).astype(np.float32))

# ---- oiseau : opacité souple par rapport au fond (orange), soleil exclu
o_minus_bg = np.array(ORANGE, np.float32) - bg
alpha = np.clip(((left - bg) @ o_minus_bg) / (o_minus_bg @ o_minus_bg), 0, 1)
yy, xx = np.mgrid[0:H, 0:W // 2]
alpha[(xx - sx) ** 2 + (yy - sy) ** 2 < (sr + 7) ** 2] = 0
alpha[alpha < 0.04] = 0

ys, xs = np.where(alpha > 0.5)
bx0, bx1, by0, by1 = xs.min(), xs.max(), ys.min(), ys.max()


def vectoriser(a, eps=1.1):
    big = cv2.resize(a, None, fx=K, fy=K, interpolation=cv2.INTER_CUBIC)
    big = cv2.GaussianBlur(big, (0, 0), 1.6)
    m = (big > 0.5).astype(np.uint8) * 255
    cs, hier = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    out = []
    for c in cs:
        if cv2.contourArea(c) < 40 * K:
            continue
        c = cv2.approxPolyDP(c, eps, True)[:, 0, :] / K
        out.append(c)
    return out


contours = vectoriser(alpha)
# boîte englobante oiseau + soleil (pour cadrer)
x0, y0 = min(bx0, sx - sr), min(by0, sy - sr)
x1, y1 = max(bx1, sx + sr), max(by1, sy + sr)
PAD = 6
x0, y0, x1, y1 = x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD
w, h = x1 - x0, y1 - y0


def path(cs, ox, oy, s=1.0):
    d = []
    for c in cs:
        pts = ['%.2f %.2f' % ((x - ox) * s, (y - oy) * s) for x, y in c]
        d.append('M' + ' L'.join(pts) + 'Z')
    return ''.join(d)


# ---- logo du site : cadre carré autour de l'oiseau + soleil
side = max(w, h)
ox, oy = x0 - (side - w) / 2, y0 - (side - h) / 2
S = 64.0 / side
bird_d = path(contours, ox, oy, S)
sun_c = ((sx - ox) * S, (sy - oy) * S, sr * S)


def mark_svg(bird, sun):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><path fill="%s" fill-rule="evenodd" d="%s"/>'
            '<circle cx="%.2f" cy="%.2f" r="%.2f" fill="%s"/></svg>' % (bird, bird_d, sun_c[0], sun_c[1], sun_c[2], sun))


os.makedirs(ROOT + 'img', exist_ok=True)
open(ROOT + 'img/logo-mark.svg', 'w', encoding='utf-8', newline='\n').write(mark_svg(HEX_O, HEX_S))


# ---- favicon rond : disque orange, motif blanc centré dans la zone sûre
def fav_svg(frac=0.64, square=False):
    s = 64 * frac / side
    off = (64 - side * s) / 2
    bd = path(contours, ox, oy, s)
    cx, cy, r = (sx - ox) * s + off, (sy - oy) * s + off, sr * s
    shape = '<rect width="64" height="64" fill="%s"/>' % HEX_O if square else '<circle cx="32" cy="32" r="32" fill="%s"/>' % HEX_O
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">%s<g transform="translate(%.2f %.2f)"><path fill="#FFFFFF" fill-rule="evenodd" d="%s"/>'
            '<circle cx="%.2f" cy="%.2f" r="%.2f" fill="%s"/></g></svg>' % (shape, off, off, bd, cx - off, cy - off, r, HEX_S))


open(ROOT + 'favicon.svg', 'w', encoding='utf-8', newline='\n').write(fav_svg())

# ---- PNG : rendu direct depuis les contours vectorisés (sur-échantillonné x4)
def raster(size, frac, bg_color=None, bird_color=(255, 255, 255), circle=True, transparent_bg=False):
    SS = 4
    N = size * SS
    img = Image.new('RGBA', (N, N), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    if bg_color is not None:
        if circle:
            dr.ellipse((0, 0, N - 1, N - 1), fill=bg_color + (255,))
        else:
            dr.rectangle((0, 0, N, N), fill=bg_color + (255,))
    s = N * frac / side
    off = (N - side * s) / 2
    m = Image.new('L', (N, N), 0)
    md = ImageDraw.Draw(m)
    # remplissage pair/impair : on dessine chaque contour en alternant (extérieur puis trous)
    for c in sorted(contours, key=lambda c: -cv2.contourArea(c.astype(np.float32))):
        pts = [((x - ox) * s + off, (y - oy) * s + off) for x, y in c]
        inside = m.getpixel((int(pts[0][0]), int(pts[0][1]))) > 0
        md.polygon(pts, fill=0 if inside else 255)
    bird = Image.new('RGBA', (N, N), bird_color + (255,))
    img.paste(bird, (0, 0), m)
    cx, cy, r = (sx - ox) * s + off, (sy - oy) * s + off, sr * s
    dr = ImageDraw.Draw(img)
    dr.ellipse((cx - r, cy - r, cx + r, cy + r), fill=SUN + (255,))
    return img.resize((size, size), Image.LANCZOS)


for size in (48, 192, 512):
    raster(size, 0.64, ORANGE).save(ROOT + 'favicon-%d.png' % size)
raster(512, 0.64, ORANGE).save(ROOT + 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
raster(180, 0.60, ORANGE, circle=False).convert('RGB').save(ROOT + 'apple-touch-icon.png')
raster(512, 0.94, None, bird_color=ORANGE).save(ROOT + 'img/logo-512.png')
print('logo et favicon générés : %d contours, boîte %dx%d' % (len(contours), w, h))
print('rapport L/H de la marque :', round(w / h, 3))
