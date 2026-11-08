"""Captures pleine page d'une page du site, à plusieurs largeurs.

Usage :
    python tools/shoot.py <url> <dossier_sortie> [largeurs...] [--scale=0.6]

Exemple :
    python tools/shoot.py http://localhost:8090/index.html shots/home 1440 390 --scale=0.6

Produit <dossier_sortie>/<largeur>.png (pleine page, taille réelle) et des tranches
<largeur>-partN.png (1600 px de haut avant réduction), réduites par --scale
(défaut 0.6) pour rester légères à relire. Utilise le Chrome installé
(channel="chrome"), sans téléchargement de navigateur.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright
from PIL import Image

SLICE = 1600


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
    url, out = args[0], Path(args[1])
    widths = [int(w) for w in args[2:]] or [1440, 390]
    scale = float(flags.get("scale", "0.6"))
    out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(channel="chrome")
        except Exception:
            browser = p.chromium.launch()
        for w in widths:
            page = browser.new_page(viewport={"width": w, "height": 900}, device_scale_factor=1)
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.goto(url, wait_until="networkidle")
            # Masque la bannière cookies et force l'affichage des éléments animés.
            page.add_style_tag(content=".cookie{display:none!important}.reveal{opacity:1!important;transform:none!important}")
            # Défile toute la page pour déclencher les images en chargement différé.
            page.evaluate("""async () => { const h = document.documentElement.scrollHeight;
              for (let y = 0; y < h; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
              window.scrollTo(0, 0); }""")
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(400)
            overflow = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
            full = out / f"{w}.png"
            page.screenshot(path=str(full), full_page=True)
            page.close()

            img = Image.open(full)
            parts = 0
            for i, top in enumerate(range(0, img.height, SLICE), start=1):
                part = img.crop((0, top, img.width, min(top + SLICE, img.height)))
                if scale != 1:
                    part = part.resize((max(1, int(part.width * scale)), max(1, int(part.height * scale))), Image.LANCZOS)
                part.save(out / f"{w}-part{i}.png")
                parts = i
            note = f" DÉBORDEMENT HORIZONTAL {overflow}px" if overflow > 0 else ""
            errs = f" ERREURS: {errors}" if errors else ""
            print(f"{full} ({img.width}x{img.height}) -> {parts} tranches{note}{errs}")
        browser.close()


if __name__ == "__main__":
    main()
