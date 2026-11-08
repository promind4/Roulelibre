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
    var page = location.pathname.split('/').pop() || 'index.html';
    var spy = [];
    nav.querySelectorAll('a[href*="#"]:not(.btn)').forEach(function (a) {
      var parts = a.getAttribute('href').split('#');
      var target = parts[1] && document.getElementById(parts[1]);
      if ((parts[0] || page) === page && target) spy.push({ a: a, el: target });
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
