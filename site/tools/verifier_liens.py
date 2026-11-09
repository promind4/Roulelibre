# -*- coding: utf-8 -*-
"""Vérifie les liens internes et les images de toutes les pages du sitemap, en résolvant chaque lien depuis l'URL réelle
de la page (comme un navigateur). Fonctionne sur le serveur local imitant Vercel (python tools/serve.py) ou sur le site en ligne.
    python tools/verifier_liens.py [http://localhost:8090]
Code de sortie : 0 = tout est bon, 1 = liens cassés."""
import re, sys, urllib.request, urllib.parse, urllib.error

BASE = (sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8090').rstrip('/')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'verif-liens'})
    try:
        r = urllib.request.urlopen(req, timeout=8)
        return r.status, r.geturl(), r.read()
    except urllib.error.HTTPError as e:
        return e.code, url, b''
    except Exception as e:
        return 0, url, str(e).encode()


sm = get(BASE + '/sitemap.xml')[2].decode('utf-8', 'replace')
pages = [urllib.parse.urlsplit(u).path or '/' for u in re.findall(r'<loc>([^<]+)</loc>', sm)]
cache, bad, n = {}, [], 0
for path in pages:
    url = BASE + path
    st, final, body = get(url)
    if st != 200:
        bad.append((path, url, st)); continue
    html = body.decode('utf-8', 'replace')
    html = re.sub(r'<script[^>]*type="application/ld\+json".*?</script>', '', html, flags=re.S)
    refs = set(re.findall(r'(?:href|src)="([^"]+)"', html))
    for s in re.findall(r'srcset="([^"]+)"', html):
        refs.update(p.strip().split(' ')[0] for p in s.split(','))
    for r in refs:
        if re.match(r'(https?:|mailto:|tel:|data:|#|javascript:)', r) and not r.startswith(BASE):
            continue
        target = urllib.parse.urljoin(final, r.split('#')[0])
        if not target.startswith(BASE) or not target.split('?')[0].strip('/'):
            if target.rstrip('/') != BASE:
                continue
        if target not in cache:
            cache[target] = get(target)[0]; n += 1
        if cache[target] != 200:
            bad.append((path, r, cache[target]))
print('%d pages, %d liens et ressources distincts testés' % (len(pages), n))
if bad:
    for p, r, s in bad:
        print('CASSÉ  %-62s %-60s %s' % (p, r, s))
    sys.exit(1)
print('Tout est bon.')
