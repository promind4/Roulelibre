# -*- coding: utf-8 -*-
"""Serveur local qui imite Vercel (cleanUrls : /conseils/mon-article sert conseils/mon-article.html, et .html est redirigé).
    python tools/serve.py [port]      (sert le dossier du site)
Sert exactement les mêmes adresses qu'en production, ce qui permet de détecter les liens relatifs cassés."""
import os, sys, http.server, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8090


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def do_GET(self):
        p = urllib.parse.urlsplit(self.path)
        path = urllib.parse.unquote(p.path)
        # /x.html -> 308 /x ; /x/index.html -> 308 /x (comme cleanUrls)
        if path.endswith('.html') and not getattr(self, '_interne', False):
            clean = path[:-5]
            if clean.endswith('/index'):
                clean = clean[:-6] or '/'
            if clean == '/index':
                clean = '/'
            self.send_response(308)
            self.send_header('Location', clean + ('?' + p.query if p.query else ''))
            self.end_headers()
            return
        full = os.path.join(ROOT, path.lstrip('/'))
        # /dossier/ -> 308 /dossier (trailingSlash: false), et /dossier sert dossier/index.html
        if path != '/' and path.endswith('/'):
            self.send_response(308)
            self.send_header('Location', path.rstrip('/') + ('?' + p.query if p.query else ''))
            self.end_headers()
            return
        if path != '/' and os.path.isdir(full) and os.path.exists(os.path.join(full, 'index.html')):
            self.path = path + '/index.html' + ('?' + p.query if p.query else '')
            return super().do_GET()
        # /x -> x.html si le fichier existe
        if path != '/' and not os.path.exists(full) and os.path.exists(full + '.html'):
            self.path = path + '.html' + ('?' + p.query if p.query else '')
        return super().do_GET()

    def end_headers(self):
        # Pas de cache en local : le navigateur affiche toujours la dernière version générée
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *a):
        pass


if __name__ == '__main__':
    http.server.ThreadingHTTPServer(('', PORT), Handler).serve_forever()
