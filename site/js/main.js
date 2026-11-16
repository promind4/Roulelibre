/* Roulelibre — comportements communs à toutes les pages :
   en-tête au défilement, menu mobile, apparitions au scroll, bandeau cookies. */
(function () {
  'use strict';
  document.documentElement.classList.remove('no-js');

  /* ---------- En-tête : filet au défilement ---------- */
  var header = document.querySelector('[data-header]');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Menu mobile ---------- */
  var burger = document.querySelector('[data-burger]');
  var nav = document.querySelector('[data-nav]');
  if (burger && nav) {
    var setOpen = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
      nav.classList.toggle('is-open', open);
    };
    burger.addEventListener('click', function () {
      setOpen(burger.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { setOpen(false); burger.focus(); }
    });
    var desktop = window.matchMedia('(min-width: 1281px)');
    var onChange = function (e) { if (e.matches) setOpen(false); };
    if (desktop.addEventListener) desktop.addEventListener('change', onChange);
    else if (desktop.addListener) desktop.addListener(onChange);
  }

  /* ---------- Menu : rubrique allumée selon la section visible ----------
     Pour les liens qui pointent vers une ancre de la page courante (accueil : La gamme,
     Service tout couvert). Avant la première section, la première rubrique reste allumée. */
  if (nav) {
    var norm = function (p) { return p.replace(/\.html$/, '').replace(/\/index$/, '/') || '/'; };
    var spy = [];
    nav.querySelectorAll('a[href*="#"]:not(.btn)').forEach(function (a) {
      var parts = a.getAttribute('href').split('#');
      var target = parts[1] && document.getElementById(parts[1]);
      var same = !parts[0] || norm(new URL(parts[0], location.href).pathname) === norm(location.pathname);
      if (same && target) spy.push({ a: a, el: target });
    });
    if (spy.length) {
      var setCurrent = function (item) {
        spy.forEach(function (s) {
          if (s === item) s.a.setAttribute('aria-current', 'page'); else s.a.removeAttribute('aria-current');
        });
      };
      var onSpy = function () {
        var line = (header ? header.offsetHeight : 0) + window.innerHeight * 0.3;
        var cur = spy[0];
        spy.forEach(function (s) { if (s.el.getBoundingClientRect().top <= line) cur = s; });
        setCurrent(cur);
      };
      var ticking = false;
      window.addEventListener('scroll', function () {
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(function () { ticking = false; onSpy(); });
      }, { passive: true });
      window.addEventListener('resize', onSpy);
      window.addEventListener('hashchange', onSpy);
      onSpy();
    }
  }

  /* ---------- Apparitions au scroll ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- Bandeau cookies (refus aussi simple que l'acceptation) ---------- */
  var KEY = 'ae-consent-v1';
  var banner = document.querySelector('[data-cookie]');
  if (!banner) return;
  var prefs = banner.querySelector('[data-cookie-prefs]');
  var more = banner.querySelector('[data-cookie-customize]');
  var opts = banner.querySelectorAll('[data-cookie-opt]');

  var MAX_AGE = 182 * 24 * 3600 * 1000; /* choix redemandé après 6 mois (recommandation CNIL) */
  var read = function () {
    var c;
    try { c = JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; }
    if (!c || !c.date || Date.now() - Date.parse(c.date) > MAX_AGE) return null;
    return c;
  };
  var write = function (choice) {
    choice.date = new Date().toISOString();
    try { localStorage.setItem(KEY, JSON.stringify(choice)); } catch (e) { /* stockage indisponible */ }
    document.dispatchEvent(new CustomEvent('consent:change', { detail: choice }));
  };
  var show = function () {
    var saved = read();
    opts.forEach(function (o) { o.checked = !!(saved && saved[o.getAttribute('data-cookie-opt')]); });
    banner.hidden = false;
  };
  var hide = function () {
    banner.hidden = true;
    if (prefs) prefs.hidden = true;
    if (more) more.setAttribute('aria-expanded', 'false');
  };
  var all = function (value) {
    var c = {};
    opts.forEach(function (o) { c[o.getAttribute('data-cookie-opt')] = value; });
    return c;
  };

  banner.addEventListener('click', function (e) {
    var t = e.target.closest('button');
    if (!t) return;
    if (t.hasAttribute('data-cookie-accept')) { write(all(true)); hide(); }
    else if (t.hasAttribute('data-cookie-refuse')) { write(all(false)); hide(); }
    else if (t.hasAttribute('data-cookie-customize') && prefs) {
      var open = prefs.hidden;
      prefs.hidden = !open;
      t.setAttribute('aria-expanded', String(open));
    } else if (t.hasAttribute('data-cookie-save')) {
      var c = {};
      opts.forEach(function (o) { c[o.getAttribute('data-cookie-opt')] = o.checked; });
      write(c); hide();
    }
  });
  document.querySelectorAll('[data-cookie-open]').forEach(function (b) {
    b.addEventListener('click', function () { show(); var first = banner.querySelector('button'); if (first) first.focus(); });
  });

  if (!read()) show();
})();

/* Mesure d'audience (Umami auto-hébergé, sans cookie, anonyme) : parcours détaillé de chaque visite.
   Chaque événement apparaît dans la fiche de la session (Umami > Sessions) et dans Événements.
   Sans effet si Umami n'est pas chargé (local, bloqueur, « Do Not Track »). */
(function () {
  'use strict';
  // Interrupteur propriétaire : ouvrir n'importe quelle page avec ?umami=off exclut ce navigateur des statistiques (?umami=on le réactive).
  // Umami lit lui-même la clé « umami.disabled » dans le stockage local.
  try {
    var q = /[?&]umami=(on|off)/.exec(location.search);
    if (q) { if (q[1] === 'off') localStorage.setItem('umami.disabled', '1'); else localStorage.removeItem('umami.disabled'); }
  } catch (e) { /* stockage indisponible */ }
  function exclu() { try { return !!localStorage.getItem('umami.disabled'); } catch (e) { return false; } }
  function ok() { return !exclu() && window.umami && typeof window.umami.track === 'function'; }
  function track(nom, data) {
    if (!ok()) return;
    data = data || {};
    data.page = location.pathname;
    try { window.umami.track(nom, data); } catch (err) { /* jamais bloquant */ }
  }
  function texte(el) { return ((el && (el.getAttribute('aria-label') || el.textContent)) || '').replace(/\s+/g, ' ').trim().slice(0, 60); }
  function zone(el) {
    if (el.closest('header')) return 'en-tete';
    if (el.closest('footer')) return 'pied';
    if (el.closest('[data-cookie]')) return 'bandeau-cookies';
    var s = el.closest('section[id], section[aria-labelledby], article, aside, main');
    return s ? (s.id || s.getAttribute('aria-labelledby') || s.tagName.toLowerCase()) : 'page';
  }
  function produit(href) {
    var h = decodeURIComponent(href);
    return /agaru-ultra/.test(h) ? 'agaru-ultra' : /agaru-smart/.test(h) ? 'agaru-smart' : /augment-360|360/.test(h) ? 'escooter-360' : 'autre';
  }

  // Clics : liens partenaires, vidéos, liens sortants, menu, liens et boutons internes, galerie, cookies
  document.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target.closest('a[href], button, summary') : null;
    if (!t) return;
    if (t.tagName === 'A') {
      var href = t.getAttribute('href') || '';
      if (/awin1\.com|augment\.eco/.test(href)) track('clic-partenaire', { produit: produit(href), texte: texte(t), zone: zone(t) });
      else if (/youtube\.com|youtu\.be/.test(href)) track('video-ouverte', { titre: texte(t.closest('article, li') || t), lien: href.slice(0, 80) });
      else if (/^https?:/.test(href) && href.indexOf(location.host) < 0 && href.indexOf('roulelibre.fr') < 0) track('clic-sortant', { domaine: href.split('/')[2], texte: texte(t) });
      else if (t.closest('nav')) track('clic-menu', { cible: href, texte: texte(t), zone: zone(t) });
      else track('clic-interne', { cible: href, texte: texte(t), zone: zone(t) });
      return;
    }
    if (t.tagName === 'SUMMARY') {
      var d = t.parentElement;
      if (d && !d.open) track('faq-ouverte', { question: texte(t) });
      return;
    }
    if (t.hasAttribute('data-cookie-accept')) return track('cookies', { choix: 'accepter' });
    if (t.hasAttribute('data-cookie-refuse')) return track('cookies', { choix: 'refuser' });
    if (t.hasAttribute('data-cookie-save')) return track('cookies', { choix: 'personnaliser' });
    if (t.hasAttribute('data-view') || t.hasAttribute('data-view-prev') || t.hasAttribute('data-view-next')) {
      var m = document.querySelector('input[name="model"]:checked');
      return track('galerie-vue', { vue: t.hasAttribute('data-view') ? texte(t) : (t.hasAttribute('data-view-prev') ? 'precedente' : 'suivante'), modele: m ? m.value : '' });
    }
    if (t.classList.contains('hotspot') || t.hasAttribute('data-goto')) return track('galerie-point', { point: texte(t) });
    if (t.hasAttribute('data-m') || t.closest('.videos__filters')) return track('filtre', { valeur: t.getAttribute('data-m') || texte(t), zone: zone(t) });
    if (t.hasAttribute('data-cookie-open') || t.hasAttribute('data-cookie-customize')) return;
    track('clic-bouton', { texte: texte(t), zone: zone(t) });
  }, true);

  // Simulateur : chaque choix (modèle, formule, durée, apport, options)
  document.addEventListener('change', function (e) {
    var el = e.target;
    if (!el || !el.closest || !el.closest('main') || el.closest('[data-cookie]')) return;
    var champ = el.getAttribute('data-opt') || el.name || el.id || 'champ';
    var valeur = el.type === 'checkbox' ? (el.checked ? 'oui' : 'non') : el.value;
    track('simulateur-choix', { champ: champ, valeur: String(valeur).slice(0, 40) });
  }, true);

  // Défilement : 25, 50, 75 et 100 % de la page, une fois chacun
  var paliers = [25, 50, 75, 100], vus = {};
  function defil() {
    var h = document.documentElement, max = h.scrollHeight - h.clientHeight;
    var pct = max > 0 ? Math.round((h.scrollTop || document.body.scrollTop) / max * 100) : 100;
    paliers.forEach(function (p) { if (pct >= p && !vus[p]) { vus[p] = 1; track('defilement', { seuil: p }); } });
  }
  window.addEventListener('scroll', function () { clearTimeout(defil.t); defil.t = setTimeout(defil, 250); }, { passive: true });

  // Temps de lecture réel (onglet visible) : 30 s, 1 min, 2 min, 5 min
  var actif = 0, envoyes = {};
  setInterval(function () {
    if (document.visibilityState !== 'visible') return;
    actif += 5;
    [30, 60, 120, 300].forEach(function (s) { if (actif >= s && !envoyes[s]) { envoyes[s] = 1; track('temps-lecture', { secondes: s }); } });
  }, 5000);

  // Fin d'article atteinte (rubrique Conseils)
  var fin = document.querySelector('.art__related, .art__sources, footer');
  if (fin && 'IntersectionObserver' in window && /^\/conseils\/./.test(location.pathname)) {
    var io = new IntersectionObserver(function (en) {
      if (en[0].isIntersecting) { track('article-lu-fin', {}); io.disconnect(); }
    });
    io.observe(fin);
  }
})();
