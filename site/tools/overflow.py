"""Mesure le débordement horizontal d'une page sur une plage de largeurs.
Usage : python tools/overflow.py <url> [min] [max] [pas]"""
import sys
from playwright.sync_api import sync_playwright
url = sys.argv[1]; lo, hi, step = (int(x) for x in (sys.argv[2:5] + ['320', '1600', '20'][len(sys.argv[2:5]):]))
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome"); pg = b.new_page()
    bad = []
    for w in range(lo, hi + 1, step):
        pg.set_viewport_size({"width": w, "height": 900}); pg.goto(url, wait_until="networkidle")
        o = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
        if o > 0: bad.append(f"{w}:{o}")
    print(url, "débordements :", bad or "aucun")
    b.close()
