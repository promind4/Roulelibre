# -*- coding: utf-8 -*-
"""Rend l'image de partage (JPG 1200x630) de chaque illustration animée : python tools/rendre_og.py [id ...]
Utilise le Chrome installé (Playwright, channel chrome). Option --planche=fichier.jpg : écrit aussi une planche contact."""
import sys, os, io
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace(chr(92), '/') + '/'
ids = [a for a in sys.argv[1:] if not a.startswith('--')]
planche = [a.split('=', 1)[1] for a in sys.argv[1:] if a.startswith('--planche=')]
if not ids:
    ids = sorted(f[5:-4] for f in os.listdir(ROOT + 'img/conseils') if f.startswith('anim-') and f.endswith('.svg'))
shots = []
with sync_playwright() as p:
    b = p.chromium.launch(channel='chrome')
    pg = b.new_page(viewport={'width': 1536, 'height': 1024})
    for i in ids:
        pg.goto('file:///' + ROOT + 'img/conseils/anim-%s.svg' % i)
        pg.wait_for_timeout(1500)
        im = Image.open(io.BytesIO(pg.screenshot())).convert('RGB')
        shots.append(im)
        og = im.resize((1200, 800), Image.LANCZOS).crop((0, 85, 1200, 715))
        og.save(ROOT + 'img/conseils/anim-%s-og.jpg' % i, quality=84, optimize=True)
        print(i, 'ok')
    b.close()
if planche:
    cols, w, h = 2, 768, 512
    rows = (len(shots) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * w, rows * h), 'white')
    for k, im in enumerate(shots):
        sheet.paste(im.resize((w, h), Image.LANCZOS), ((k % cols) * w, (k // cols) * h))
    sheet.save(planche[0], quality=80)
