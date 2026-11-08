/* Roulelibre — vidéos YouTube : liste unique, cartes et lecteur intégré.

   Pour ajouter une vidéo : ajouter une ligne à VIDEOS.
   - id : identifiant YouTube (après « v= », ou après « /shorts/ »)
   - start : seconde de départ (facultatif)
   - short : true pour une vidéo verticale (YouTube Shorts)
   - model : 'agaru' ou '360' (uniquement la gamme actuelle)
   - official : true pour une vidéo publiée par Augment
   - title : titre en français (traduit si la vidéo est dans une autre langue)
   - partner : true pour une vidéo d'un partenaire commercial d'Augment (sponsoring, etc.)
   La vidéo doit autoriser l'intégration (vérifier avec https://www.youtube.com/oembed?url=<lien>).
   Le lecteur (youtube-nocookie.com) ne se charge qu'au clic du visiteur. */
(function () {
  'use strict';

  var VIDEOS = [
    { id: 'mEkZi-Sf6LI', start: 46, model: 'agaru', lang: 'Français', channel: 'La Provence Médias',
      title: '[J’ai testé pour vous] la trottinette d’Augment Eco' },
    { id: 'nDMStkJ8ILA', model: '360', lang: 'Allemand', channel: 'Scooterhelden',
      title: 'Test de l’Augment 360 : puissance, confort et autonomie' },
    { id: 'aj_WF7LTzPU', model: '360', lang: 'Allemand', channel: 'Scooterhelden',
      title: 'L’Augment 360 passé au crible : un scooter à 45 km/h qui se plie facilement ?' },
    { id: '1JlCzkj85z8', model: '360', lang: 'Allemand', channel: 'ScooterheldenLive',
      title: 'Augment 360 : direction Berlin !' },
    { id: 'I5LgCb1vusg', model: '360', lang: 'Anglais', channel: 'Ajo Motorsport', partner: true, short: true,
      title: 'On s’amuse avec notre nouvel Augment 360 !' },
    { id: 'qNRi9uKldvo', model: '360', lang: 'Français', channel: 'Augment', official: true,
      title: 'Puissant. Léger. Compact. Découvrez le scooter électrique 360 d’Augment.' },
    { id: 'fX_IZyXcZLE', model: 'agaru', lang: 'Français', channel: 'Augment', official: true, short: true,
      title: 'Augment, la trottinette sans prise de tête.' },
    { id: 'wXfl3QA_Mfs', model: 'agaru', lang: 'Français', channel: 'Augment', official: true, short: true,
      title: 'La trottinette sans prise de tête' },
    { id: 'Jm-ktmSit1Y', model: 'agaru', lang: 'Français', channel: 'Augment', official: true, short: true,
      title: 'Pourquoi acheter une trottinette alors que vous pouvez louer ?' }
  ];

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  function watchUrl(v) {
    return v.short ? 'https://www.youtube.com/shorts/' + v.id : 'https://www.youtube.com/watch?v=' + v.id + (v.start ? '&t=' + v.start + 's' : '');
  }
  function embedUrl(v) {
    return 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(v.id) +
      '?autoplay=1&rel=0&modestbranding=1&playsinline=1' + (v.start ? '&start=' + v.start : '');
  }

  function card(v, i) {
    var by = v.channel + (v.official ? ' · vidéo officielle' : '') + (v.partner ? ' · partenaire d’Augment' : '');
    return '<li class="video" data-model="' + v.model + '" data-official="' + (v.official ? '1' : '0') + '">' +
      '<div class="video__frame' + (v.short ? ' video__frame--short' : '') + '">' +
        '<button class="video__play" type="button" data-video="' + i + '" aria-label="' + esc('Lire la vidéo : ' + v.title + ', ' + v.channel) + '">' +
          '<img src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" width="480" height="360" alt="" loading="lazy" decoding="async">' +
          '<span class="video__btn" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></span>' +
        '</button>' +
      '</div>' +
      '<div class="video__body">' +
        '<h3 class="video__title">' + esc(v.title) + '</h3>' +
        '<p class="video__channel">' + esc(by) + '</p>' +
        '<a class="video__yt" href="' + esc(watchUrl(v)) + '" target="_blank" rel="noopener">Voir sur YouTube <span aria-hidden="true">↗</span></a>' +
      '</div>' +
    '</li>';
  }

  /* ---------- Cartes ---------- */
  var lists = document.querySelectorAll('[data-videos]');
  if (!lists.length) return;
  lists.forEach(function (ul) { ul.innerHTML = VIDEOS.map(card).join(''); });

  /* ---------- Carrousel (accueil) : flèches à la souris, glisser au doigt ---------- */
  document.querySelectorAll('[data-carousel]').forEach(function (box) {
    var track = box.querySelector('[data-carousel-track]');
    var prev = box.querySelector('[data-carousel-prev]');
    var next = box.querySelector('[data-carousel-next]');
    if (!track || !prev || !next) return;
    prev.hidden = next.hidden = false;
    var page = function (dir) {
      var item = track.querySelector('.video');
      var stepW = item ? item.getBoundingClientRect().width + parseFloat(getComputedStyle(track).columnGap || 0) : track.clientWidth;
      var n = Math.max(1, Math.floor(track.clientWidth / stepW));
      track.scrollBy({ left: dir * n * stepW, behavior: 'smooth' });
    };
    var update = function () {
      var max = track.scrollWidth - track.clientWidth - 2;
      prev.disabled = track.scrollLeft <= 2;
      next.disabled = track.scrollLeft >= max;
    };
    prev.addEventListener('click', function () { page(-1); });
    next.addEventListener('click', function () { page(1); });
    track.addEventListener('scroll', function () { window.requestAnimationFrame(update); }, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  /* ---------- Filtres (page Vidéos) ---------- */
  var filters = document.querySelector('[data-video-filters]');
  if (filters) {
    filters.addEventListener('change', function (e) {
      var f = e.target.value;
      document.querySelectorAll('[data-videos] .video').forEach(function (li) {
        var show = f === 'all' || (f === 'official' ? li.dataset.official === '1' : li.dataset.model === f);
        li.hidden = !show;
      });
    });
  }

  /* ---------- Lecteur intégré ---------- */
  var dlg = document.createElement('dialog');
  dlg.className = 'player';
  dlg.setAttribute('aria-labelledby', 'player-title');
  dlg.innerHTML =
    '<div class="player__box">' +
      '<div class="player__head">' +
        '<div><p class="player__meta" data-player-meta></p><h2 class="player__title" id="player-title" data-player-title></h2></div>' +
        '<button class="player__close" type="button" data-player-close aria-label="Fermer la vidéo">' +
          '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>' +
      '</div>' +
      '<div class="player__stage" data-player-stage></div>' +
      '<div class="player__foot">' +
        '<button class="btn btn--ghost btn--sm player__nav" type="button" data-player-prev><span aria-hidden="true">←</span> Précédente</button>' +
        '<a class="player__yt" href="https://www.youtube.com/" data-player-yt target="_blank" rel="noopener">Voir sur YouTube <span aria-hidden="true">↗</span></a>' +
        '<button class="btn btn--ghost btn--sm player__nav" type="button" data-player-next>Suivante <span aria-hidden="true">→</span></button>' +
      '</div>' +
    '</div>';
  document.body.appendChild(dlg);

  var current = -1, opener = null;
  var stage = dlg.querySelector('[data-player-stage]');

  function visible() {
    /* Ordre de lecture : vidéos visibles (filtre en cours) de la liste qui a ouvert le lecteur. */
    var root = opener ? opener.closest('[data-videos]') : null;
    var btns = root ? root.querySelectorAll('.video:not([hidden]) [data-video]') : [];
    var idx = [];
    btns.forEach(function (b) { idx.push(+b.getAttribute('data-video')); });
    return idx.length ? idx : VIDEOS.map(function (_, i) { return i; });
  }
  function load(i) {
    var v = VIDEOS[i];
    current = i;
    dlg.querySelector('[data-player-title]').textContent = v.title;
    dlg.querySelector('[data-player-meta]').textContent = v.channel + (v.official ? ' · vidéo officielle' : '') + (v.partner ? ' · partenaire d’Augment' : '');
    dlg.querySelector('[data-player-yt]').href = watchUrl(v);
    stage.classList.toggle('player__stage--short', !!v.short);
    stage.innerHTML = '';
    var f = document.createElement('iframe');
    f.src = embedUrl(v);
    f.title = v.title;
    f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    f.referrerPolicy = 'strict-origin-when-cross-origin';
    f.allowFullscreen = true;
    stage.appendChild(f);
    var order = visible();
    var single = order.length < 2;
    dlg.querySelector('[data-player-prev]').hidden = single;
    dlg.querySelector('[data-player-next]').hidden = single;
  }
  function step(d) {
    var order = visible();
    var pos = order.indexOf(current);
    load(order[(pos + d + order.length) % order.length]);
  }
  function close() {
    stage.innerHTML = '';            /* coupe le son et décharge le lecteur */
    if (dlg.open) dlg.close();
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-video]');
    if (!b) return;
    opener = b;
    load(+b.getAttribute('data-video'));
    if (typeof dlg.showModal === 'function') dlg.showModal(); else dlg.setAttribute('open', '');
    dlg.querySelector('[data-player-close]').focus();
  });
  dlg.addEventListener('click', function (e) {
    if (e.target === dlg || e.target.closest('[data-player-close]')) close();
    else if (e.target.closest('[data-player-prev]')) step(-1);
    else if (e.target.closest('[data-player-next]')) step(1);
  });
  dlg.addEventListener('keydown', function (e) {
    if (e.target.tagName === 'IFRAME') return;
    if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });
  dlg.addEventListener('close', function () {
    stage.innerHTML = '';
    if (opener) opener.focus();
  });
})();
