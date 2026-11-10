# -*- coding: utf-8 -*-
"""Exporte les images produits du site depuis les originaux transparents (D:\\AUGMENT ECO\\AGARU ULTRA, E SCOOTER 360...).
    python tools/images_produits.py
Cadrage = boîte englobante du produit (les points chauds de la vue A sont en % de cette image), définition d'origine
conservée (jusqu'à 1920 px), WebP qualité 90 avec transparence soignée, trois tailles : -800, -1280 et pleine taille.
Écrit aussi tools/data/images_produits.json (largeur/hauteur à reporter dans js/configurateur.js)."""
import os, json
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/') + '/'
SRC = os.path.dirname(os.path.dirname(ROOT.rstrip('/'))).replace('\\', '/') + '/'
SRC = 'D:/AUGMENT ECO/'
OUT = ROOT + 'img/'

# nom du fichier du site : (dossier source, fichier source)
MAP = {
    'agaru-profil-deplie': ('AGARU ULTRA', '01_agaru_ultra_profil_deplie.png'),
    'agaru-profil-plie': ('AGARU ULTRA', '02_agaru_ultra_profil_plie.png'),
    'agaru-cockpit': ('AGARU ULTRA', '03_agaru_ultra_cockpit_ecran_led.png'),
    'agaru-guidon-clignotants': ('AGARU ULTRA', '04_agaru_ultra_guidon_clignotants.png'),
    'agaru-plateau-frein': ('AGARU ULTRA', '05_agaru_ultra_plateau_frein_disque_arriere.png'),
    'augment-app': ('AGARU SMART', '06_augment_application_mobile.png'),
    '360-vue-3-4': ('E SCOOTER 360', '01_scooter_360_vue_3_4_deplie.png'),
    '360-roue-arriere': ('E SCOOTER 360', '04_scooter_360_roue_arriere_disque_hydraulique_charniere_orange.png'),
    '360-app': ('E SCOOTER 360', '05_augment_application_mobile.png'),
}
TAILLES = [(800, '-800'), (1280, '-1280')]

def enregistrer(im, path):
    im.save(path, 'WEBP', quality=90, method=4, alpha_quality=100, exact=False)

dims = {}
for nom, (dossier, fichier) in MAP.items():
    p = SRC + dossier + '/' + fichier
    im = Image.open(p).convert('RGBA')
    bbox = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    im = im.crop(bbox)
    w, h = im.size
    enregistrer(im, OUT + nom + '.webp')
    for cote, suf in TAILLES:
        if w > cote:  # tailles définies par la LARGEUR : les descripteurs « 800w / 1280w » du srcset restent exacts
            k = cote / float(w)
            r = im.resize((max(1, round(w * k)), max(1, round(h * k))), Image.LANCZOS)
            r = r.filter(ImageFilter.UnsharpMask(radius=0.8, percent=35, threshold=2))
            enregistrer(r, OUT + nom + suf + '.webp')
        else:
            enregistrer(im, OUT + nom + suf + '.webp')
    dims[nom] = [w, h]
    print('%-26s %4dx%-4d  %3d Ko  (%s)' % (nom, w, h, os.path.getsize(OUT + nom + '.webp') // 1024, fichier[:34]))
os.makedirs(ROOT + 'tools/data', exist_ok=True)
json.dump(dims, open(ROOT + 'tools/data/images_produits.json', 'w', encoding='utf-8'), indent=1)
