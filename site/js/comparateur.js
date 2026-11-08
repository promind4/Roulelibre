/* Comparatif, guides & FAQ — comportements propres à la page :
   mise en évidence des écarts Smart / Ultra et en-tête collant compact du tableau. */
(function () {
  'use strict';

  var table = document.getElementById('cmp-table');
  var toggle = document.querySelector('[data-hl-toggle]');
  var wrap = document.querySelector('[data-cmp]');
  if (!table) return;

  /* ---------- Écarts Smart / Ultra ---------- */
  if (toggle) {
    var apply = function () { table.classList.toggle('is-hl', toggle.checked); };
    toggle.addEventListener('change', apply);
    apply();
  }

  /* ---------- En-tête collant : version compacte une fois détaché ---------- */
  var thead = table.tHead;
  if (!wrap || !thead) return;
  var header = document.querySelector('[data-header]');
  var hdrH = 72;
  var measure = function () {
    hdrH = header ? Math.round(header.getBoundingClientRect().height) : 72;
    /* Hauteur réelle de l'en-tête du site : sert de décalage à la ligne collante. */
    document.documentElement.style.setProperty('--hdr', hdrH + 'px');
  };

  /* Pour éviter tout saut de contenu (et ne pas fausser les ancres), la hauteur perdue
     par l'en-tête compact est rendue en marge au-dessus du tableau, zone déjà sortie
     de l'écran à ce moment-là. */
  var setStuck = function (on) {
    if (on === wrap.classList.contains('is-stuck')) return;
    var before = thead.offsetHeight;
    wrap.classList.toggle('is-stuck', on);
    var d = on ? before - thead.offsetHeight : 0;
    wrap.style.paddingTop = d > 0 ? d + 'px' : '';
  };

  /* Test au défilement (et non IntersectionObserver) : fiable aussi lors d'un saut
     direct par ancre ou d'une restauration de position au rechargement. */
  var ticking = false;
  var check = function () {
    ticking = false;
    var r = wrap.getBoundingClientRect();
    setStuck(r.top < hdrH);
  };
  var onScroll = function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(check); }
  };

  measure();
  check();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('load', check);
  var timer;
  window.addEventListener('resize', function () {
    clearTimeout(timer);
    timer = setTimeout(function () {
      measure();
      /* La largeur change la hauteur de l'en-tête : on recalcule la compensation. */
      setStuck(false);
      check();
    }, 150);
  }, { passive: true });
})();
