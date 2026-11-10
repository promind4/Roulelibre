/* Roulelibre — Fiche produit & simulateur de forfait (configurateur.html)
   Données reprises à l'identique de la maquette Configurateur.dc.html
   (relevé augment.eco du 07/11/2026). Aucune donnée inventée. */
(function () {
  'use strict';


  /* ---------- Outils de formatage (typographie française) ---------- */
  var NB = ' ';   // espace insécable
  var NNB = ' ';  // milliers : espace insécable (l'espace fine U+202F n'a pas de glyphe dans les polices du site)
  function fr(s) {
    return String(s)
      .replace(/(\d) (\d{3})(?!\d)/g, '$1' + NNB + '$2')
      .replace(/ ([€%:;?!»])/g, NB + '$1')
      .replace(/« /g, '«' + NB)
      .replace(/(\d) (km\/h|km|Wh|W|Nm|kg|mois|mm|Ah|ans|batteries|batterie)(?![\wà-ÿ])/g, '$1' + NB + '$2');
  }
  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function t(s) { return esc(fr(s)); }
  function EUR(n) {
    return n.toLocaleString('fr-FR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }).replace(/[\s  ]/g, NNB) + NB + '€';
  }
  function EUR0(n) { return EUR(n).replace(',00', ''); }

  /* ---------- Vues produit ----------
     IMAGE À REMPLACER : chaque entrée « src » pointe vers une photo détourée (WebP transparent,
     recadrée au contenu). Pour remplacer une photo, garder le même nom de fichier ou mettre à jour
     src + w + h ici (les points chauds de la vue A sont en % de l'image recadrée). */
  var AGARU_VIEWS = [
    { letter: 'A', label: 'Profil déplié', src: 'img/agaru-profil-deplie.webp', w: 1589, h: 1715, main: true, posed: true,
      alt: 'Trottinette Agaru dépliée, vue de profil' },
    { letter: 'B', label: '3/4 avant', src: 'img/agaru-studio-3-4-avant.webp', w: 1536, h: 1024, studio: true,
      alt: 'Trottinette Agaru en vue de trois quarts avant, sur fond chaleureux',
      caption: 'Vue de trois quarts avant : potence rigide, roue avant de 10 pouces avec réflecteur ambre, plateau antidérapant.' },
    { letter: 'C', label: '3/4 arrière', src: 'img/agaru-studio-3-4-arriere.webp', w: 1536, h: 1024, studio: true,
      alt: 'Trottinette Agaru en vue de trois quarts arrière, sur fond chaleureux',
      caption: 'Vue de trois quarts arrière : garde-boue avec feu stop, frein à disque et réflecteur ambre.' },
    { letter: 'D', label: 'Profil plié', src: 'img/agaru-profil-plie.webp', w: 1788, h: 737, posed: true,
      alt: 'Trottinette Agaru repliée, vue de profil',
      caption: 'Trottinette repliée : potence rabattue, crochet avant engagé dans le garde-boue arrière.' },
    { letter: 'E', label: 'Cockpit LED', src: 'img/agaru-cockpit.webp', w: 1786, h: 1175,
      alt: 'Cockpit de l’Agaru : guidon, écran LED et commandes',
      caption: 'Guidon élargi, écran LED (vitesse, mode, niveau de batterie), bouton de fonction et commandes de clignotants gauche / droite.' },
    { letter: 'F', label: 'Détail marque', src: 'img/agaru-studio-detail-marque.webp', w: 1536, h: 1024, studio: true,
      alt: 'Gros plan sur la potence de l’Agaru et son inscription augment°',
      caption: 'Gros plan : potence en alliage noir mat, marque augment° et écran LED.' },
    { letter: 'G', label: 'Détail frein arrière', src: 'img/agaru-plateau-frein.webp', w: 1805, h: 1642,
      alt: 'Plateau de l’Agaru et frein à disque arrière',
      caption: 'Plateau avec batterie fixe intégrée, feu stop arrière et étrier de frein à disque mécanique arrière sur pneu 10 × 2,5 pouces.' },
    { letter: 'H', label: 'Au quotidien', src: 'img/photo-quotidien.webp', w: 1536, h: 1024, photo: true,
      alt: 'Un homme en manteau et baskets blanches traverse une place ensoleillée en trottinette Agaru',
      caption: 'Au quotidien : légère et pliable, jusqu’à 25 km/h. Casque conseillé.' }
  ];
  var S360_VIEWS = [
    { letter: 'A', label: 'Vue 3/4 dépliée', src: 'img/360-vue-3-4.webp', w: 1387, h: 1209, main: true, posed: true,
      alt: 'E-scooter 360 déplié, vue de trois quarts avant' },
    { letter: 'B', label: 'Profil', src: 'img/360-studio-profil.webp', w: 1536, h: 1024, studio: true,
      alt: 'E-scooter 360 en vue de profil, sur fond chaleureux',
      caption: 'De profil : cadre en un seul arc, colonne de batterie amovible sous la selle, pneus larges de 12 pouces.' },
    { letter: 'C', label: '3/4 avant', src: 'img/360-studio-3-4-avant.webp', w: 1536, h: 1024, studio: true,
      alt: 'E-scooter 360 en vue de trois quarts avant, sur fond chaleureux',
      caption: 'Trois quarts avant : guidon avec rétroviseur, fourche noire, frein à disque avant.' },
    { letter: 'D', label: 'Roue arrière', src: 'img/360-roue-arriere.webp', w: 1446, h: 1638,
      alt: 'E-scooter 360, roue arrière, frein à disque et molette orange de pliage',
      caption: 'Pneu 120/90-R10, frein à disque hydraulique arrière, support de plaque et molette orange de déverrouillage du pliage.' },
    { letter: 'E', label: 'En ville', src: 'img/photo-360-ville.webp', w: 1536, h: 1024, photo: true,
      alt: 'Un homme en veste de cuir roule en E-scooter 360 dans une rue ensoleillée, casque et gants portés',
      caption: 'En ville, jusqu’à 45 km/h. Casque et gants obligatoires.' },
    { letter: 'F', label: 'Le week-end', src: 'img/photo-weekend.webp', w: 1536, h: 1024, photo: true,
      alt: 'E-scooter 360 garé devant une terrasse de café, casque et gants posés sur la selle',
      caption: 'Le week-end : le 360 garé devant un café, casque et gants posés sur la selle.' }
  ];

  /* ---------- Points clés (points chauds de la vue A) — x / y en % de l'image recadrée ---------- */
  function agaruPoints(M) {
    return [
      { n: '01', x: 27, y: 7, title: 'Guidon élargi & écran LED', text: (M.key === 'ultra' ? 'Clignotants intégrés aux poignées (option gratuite)' : 'Clignotants (extra gratuit au tunnel de commande)') + ', bouton multifonction et verrouillage via l’application mobile.' },
      { n: '02', x: 55, y: 87, title: 'Plateau central', text: 'Batterie Li-ion fixe intégrée au plateau : ' + M.battery + ' (' + M.batteryOther + '). Étanchéité IPX5.' },
      { n: '03', x: 11, y: 87, title: 'Roue avant', text: 'Moteur 500 W (800 W crête), couple 26 Nm, pentes jusqu’à 23 %. Freinage électronique eABS à l’avant.' },
      { n: '04', x: 88, y: 88, title: 'Roue arrière', text: 'Pneus à air 10 × 2,5 pouces. Frein à disque mécanique à l’arrière.' }
    ];
  }
  var S360_POINTS = [
    { n: '01', x: 72, y: 30, title: 'Selle à ouverture par bouton & écran NFC', text: 'Démarrage sans clé par badge NFC. Logement pour 1 ou 2 batteries amovibles de 1 080 Wh (5,2 kg l’unité), jusqu’à 106 km.' },
    { n: '02', x: 66, y: 74, title: 'Charnière centrale à molette orange', text: 'Pliage compact (1265 × 350 × 1180 mm) pour un rangement en appartement, ascenseur ou bureau. Cadre aluminium garanti 5 ans.' },
    { n: '03', x: 84, y: 80, title: 'Roue arrière', text: 'Moteur 2 140 W à fort couple (105 Nm), 45 km/h, catégorie L1e. Blocage antivol de la roue arrière via l’application.' },
    { n: '04', x: 16, y: 78, title: 'Trains roulants', text: 'Pneus larges tubeless 120/90-R10 (18.5"), compatibles pneus hiver. Freins à disque hydrauliques.' }
  ];

  /* ---------- Fiches techniques ---------- */
  function AGARU_SPECS(km, cap, kg) {
    return [
      ['Catégorie', 'EDPM (e-trottinette)'], ['Vitesse max', '25 km/h'], ['Moteur', '500 W'], ['Puissance maximale', '800 W'],
      ['Couple', '26 Nm'], ['Montée en pente', '23 %'], ['Autonomie max', km], ['Batterie', 'Fixe, intégrée au plateau'],
      ['Capacité', cap], ['Type de batterie', 'Li-ion'], ['Pneus', 'pneus à air 10 × 2,5 pouces'], ['Poids', kg],
      ['Freins', 'Disque mécanique à l’arrière + eABS à l’avant'], ['Étanchéité', 'IPX5']
    ];
  }
  var SPEC_GROUPS = [
    ['Performances', ['Catégorie', 'Vitesse max', 'Moteur', 'Puissance maximale', 'Couple', 'Montée en pente', 'Autonomie max']],
    ['Batterie', ['Batterie', 'Capacité', 'Type de batterie']],
    ['Châssis & freinage', ['Pneus', 'Freins', 'Étanchéité', 'Poids']],
    ['Dimensions & garantie', ['Dimensions déplié', 'Dimensions plié', 'Garantie']]
  ];

  /* ---------- Modèles ---------- */
  var MODELS = {
    smart: {
      key: 'smart', idx: '01', name: 'Agaru Smart', tagline: 'Le choix malin', cls: 'EDPM 25 km/h', agaru: true,
      grid: [['Poids', '20,0 kg'], ['Autonomie', '50 km'], ['Batterie', '499 Wh fixe'], ['Moteur', '500W / 800W']],
      purchase: 399, sub: null,
      /* Avec couverture contre le vol (70,80 € ajoutés au montant financé) : relevé au tunnel augment.eco. */
      fin: function (vol) { return vol ? { monthly: 22.75, total: 546.11, months: '24 mois', withVol: true } : { monthly: 19.33, total: 463.78, months: '24 mois' }; },
      battery: '499 Wh', batteryOther: '768 Wh sur l’Ultra',
      specs: AGARU_SPECS('50 km', '10,4 Ah / 499 Wh', '20 kg'),
      stats: [['Autonomie', '50', 'km', 'Autonomie max'], ['Vitesse max', '25', 'km/h', 'EDPM (e-trottinette)'], ['Batterie', '499', 'Wh', 'Fixe, intégrée au plateau'], ['Poids', '20', 'kg', '']],
      equip: ['Clignotants', 'Un guidon plus large', 'Application mobile', 'Antivol digital', 'Batterie 10.4Ah / 499Wh intégrée dans le plateau', 'Charge rapide', 'Moteur surpuissant', 'Pliage rapide', 'Étanchéité IPX5', 'Pneus à air 10 x 2,5 pouces', 'Double système de freinage'],
      quote: '« Agaru Smart, c’est la mobilité sans stress et sans faille. Une e-trottinette solide, fiable et prête à affronter le quotidien. »'
    },
    ultra: {
      key: 'ultra', idx: '02', name: 'Agaru Ultra', tagline: 'La meilleure autonomie', cls: 'EDPM 25 km/h', agaru: true,
      grid: [['Poids', '20,7 kg'], ['Autonomie', '70 km'], ['Batterie', '768 Wh fixe'], ['Moteur', '500W / 800W']],
      purchase: 549,
      /* Grille relevée au configurateur augment.eco le 07/11/2026 : prix mensuel de base et économie totale, par durée et par palier d'acompte. */
      sub: {
        acomptes: [59, 119, 189, 249, 399],
        prices: { 12: [44.95, 38.95, 32.95, 26.95, 12.95], 24: [32.95, 29.95, 25.95, 22.95, 14.95], 36: [29.95, 26.95, 23.95, 21.95, 16.95] },
        savings: { 12: [0, 12, 14, 26, 44], 24: [0, 12, 38, 50, 92], 36: [0, 48, 86, 98, 128] }
      },
      fin: function () { return { monthly: 26.59, total: 638.19, months: '24 mois' }; },
      battery: '768 Wh', batteryOther: '499 Wh sur le Smart',
      specs: AGARU_SPECS('70 km', '16 Ah / 768 Wh', '20,7 kg'),
      stats: [['Autonomie', '70', 'km', 'Autonomie max'], ['Vitesse max', '25', 'km/h', 'EDPM (e-trottinette)'], ['Batterie', '768', 'Wh', 'Fixe, intégrée au plateau'], ['Poids', '20,7', 'kg', '']],
      equip: ['Visibilité renforcée', 'Clignotants intégrés aux poignées', 'Un guidon plus large', 'Application mobile', 'Antivol digital', 'Batterie 16Ah / 768Wh intégrée dans le plateau', 'Moteur surpuissant', 'Pliage rapide', 'Étanchéité IPX5', 'Pneus à air 10 x 2,5 pouces', 'Double système de freinage'],
      quote: '« L’Agaru Ultra est la seule trottinette en leasing privé offrant une autonomie allant jusqu’à 70 km. »'
    },
    '360': {
      key: '360', idx: '03', name: 'E-scooter 360', tagline: 'Léger. Puissant. Rapide.', cls: 'L1e 45 km/h', agaru: false,
      grid: [['Poids', '36 kg (31 kg vide)'], ['Autonomie', '53 / 106 km'], ['Batterie', '1080 Wh amovible'], ['Moteur', '2140 W (105 Nm)']],
      purchase: 1990,
      sub: {
        acomptes: [290, 590, 890, 1190, 1490],
        prices: { 12: [159.90, 132.90, 106.90, 79.90, 51.90], 24: [89.90, 74.90, 59.90, 42.90, 27.90], 36: [64.90, 55.90, 46.90, 36.90, 25.90] },
        savings: { 12: [0, 24, 36, 60, 96], 24: [0, 60, 120, 228, 288], 36: [0, 24, 48, 108, 204] }
      },
      fin: function () { return { monthly: 96.38, total: 2313.24, months: '24 mois' }; },
      specs: [
        ['Catégorie', 'L1e (cyclomoteur)'], ['Vitesse max', '45 km/h'], ['Moteur', '2 140 W'], ['Couple', '105 Nm'],
        ['Montée en pente', 'Non communiquée'], ['Autonomie max', '53 km (1 batterie) / 106 km (2 batteries)'],
        ['Batterie', 'Amovible, 5,2 kg par batterie'], ['Capacité', '1 080 Wh'], ['Type de batterie', 'Li-ion 21700'],
        ['Pneus', '120/90-R10, 18.5", tubeless, compatibles pneus hiver'], ['Poids', '36 kg avec batterie, 31 kg à vide'],
        ['Freins', 'Freins à disque hydrauliques'], ['Étanchéité', 'IPX4'], ['Dimensions déplié', '1555 × 609 × 1010 mm'],
        ['Dimensions plié', '1265 × 350 × 1180 mm'], ['Garantie', '2 ans, 5 ans sur le cadre aluminium']
      ],
      stats: [['Autonomie', '53', 'km', '1 batterie · 106 km avec 2 batteries'], ['Vitesse max', '45', 'km/h', 'L1e (cyclomoteur)'], ['Batterie', '1 080', 'Wh', 'Amovible, 5,2 kg par batterie'], ['Poids', '36', 'kg', '36 kg avec batterie, 31 kg à vide']],
      equip: ['Commandes et verrouillage via l’app', 'Badge NFC', 'Selle à ouverture par bouton', 'Fini le parking : rangement en intérieur', 'Roulez par tous les temps : IPX4', 'Pneus larges 120/90-R10'],
      quote: '« Démarrage par contact du badge NFC sur l’écran. La selle s’ouvre via un bouton pour un accès direct à la batterie et à l’espace de stockage. »'
    }
  };

  var TEXT = {
    smartNote: 'Abonnement non ouvert pour l’Agaru Smart dans le tunnel FR. Accroche affichée sur augment.eco : « 23,95 €/mois, avec 23 € d’apport. »',
    vol360: 'Couverture contre le vol des trottinettes : non applicable automatiquement au 360. Une éventuelle protection se confirme séparément auprès d’Augment.',
    credit: 'Un crédit vous engage et doit être remboursé. Vérifiez vos capacités de remboursement avant de vous engager.',
    creditMore: 'Financement opéré par PayPal. D’autres durées de remboursement peuvent être proposées lors du paiement.',
    serviceSmart: 'Service Agaru : réparations et remplacements couverts, disponible en option à l’achat (tarif sur augment.eco).',
    serviceUltraSub: 'Service Agaru inclus dans l’abonnement : « Réparations et remplacements gratuits. Tout est couvert. »',
    serviceUltraBuy: 'Service de réparation tout compris disponible en option à l’achat (tarif sur augment.eco).',
    service360: 'E-scooter 360 : pièces d’usure disponibles, réparation tout compris non incluse. Garantie 2 ans, 5 ans sur le cadre aluminium.',
    volBuy: 'Couverture contre le vol à l’achat : 70,80 € pour 24 mois, réglés à la commande.',
    volFin: 'Couverture contre le vol : mensualité avec couverture non affichée par Augment, précisée lors du paiement. Exemple ci-dessus pour le véhicule seul.',
    fin360: 'Augment affiche aussi pour le 360 la mention « Financement partenaire (bientôt disponible) ».',
    appAgaru: 'Statistiques de trajet, état de la batterie et antivol digital depuis le smartphone.',
    app360: 'Modes de conduite, paramètres et protection antivol : une fois activée, le 360 réagit au moindre mouvement en verrouillant la roue arrière.'
  };

  var VOL = 2.95;        /* couverture contre le vol en abonnement, €/mois */
  var VOL_BUY = 70.80;   /* couverture contre le vol à l'achat : 24 mois payés à la commande */
  var HELMET_BUY = 39;   /* casque Alpina Soho à l'achat */
  var HELMET_SUB = 1.62; /* casque en abonnement : taille S (1,65 €/mois en M/L) */

  /* ==========================================================================
     Logique de prix (portée telle quelle de la maquette)
     ========================================================================== */
  function computeOffer(st) {
    var M = MODELS[st.model];
    var mode = ((st.mode === 'sub' && !M.sub) || (st.mode === 'fin' && !M.fin)) ? 'buy' : st.mode;
    var row = function (label, value, strong) { return { label: label, value: value, strong: !!strong }; };
    var is360 = M.key === '360';
    var volOn = !!(M.agaru && st.vol);
    var helmetMonthly = mode === 'sub' && st.helmet;
    var oneTime = (st.helmet && !helmetMonthly ? HELMET_BUY : 0) + (is360 && st.battery ? 690 : 0);
    var oneTimeRows = function () {
      var r = [];
      if (M.agaru && st.signals) r.push(row('Clignotants Agaru', EUR(0)));
      if (st.helmet && !helmetMonthly) r.push(row('Casque Alpina Soho', '+ ' + EUR(HELMET_BUY)));
      if (is360 && st.battery) r.push(row('2e batterie 1 080 Wh', '+ ' + EUR(690)));
      return r;
    };
    var o = { mode: mode, recap: [], extras: [], credit: null, sub: null };

    if (mode === 'sub') {
      var dur = st.dur, ac = st.ac;
      var base = M.sub.prices[dur][ac];
      var saving = M.sub.savings[dur][ac];
      var acompte = M.sub.acomptes[ac];
      var monthly = base + (volOn ? VOL : 0) + (helmetMonthly ? HELMET_SUB : 0);
      o.sub = { dur: dur, ac: ac, saving: saving, savingMax: M.sub.savings[dur][4], acomptes: M.sub.acomptes };
      o.price = {
        label: 'Total mensuel', big: EUR(monthly), unit: '/ mois',
        sub: monthly !== base ? 'dont ' + EUR(base) + ' de prix mensuel de base' + (volOn ? ' + ' + EUR(VOL) + ' de couverture contre le vol' : '') + (helmetMonthly ? ' + ' + EUR(HELMET_SUB) + ' de casque (taille S)' : '') : 'Prix mensuel de base, sans option mensuelle',
        terms: 'Durée minimale ' + dur + ' mois · acompte ' + EUR(acompte) + (oneTime ? ' · extras ' + EUR(oneTime) + ' à la commande' : '')
      };
      o.recap.push(row('Prix mensuel de base', EUR(base)));
      if (volOn) o.recap.push(row('Couverture contre le vol', '+ ' + EUR(VOL)));
      if (helmetMonthly) o.recap.push(row('Casque Alpina Soho (taille S)', '+ ' + EUR(HELMET_SUB)));
      o.recap.push(row('Total mensuel', EUR(monthly), true));
      o.recap.push(row('Acompte', EUR(acompte)));
      o.recap = o.recap.concat(oneTimeRows());
      o.recap.push(row('Économie totale sur ' + dur + ' mois', EUR(saving)));
      o.total = { label: 'Total mensuel', value: EUR(monthly), unit: '/ mois' };
      o.extras.push('Acompte ' + EUR(acompte));
      if (oneTime) o.extras.push('extras + ' + EUR(oneTime));
    } else if (mode === 'buy') {
      var volCost = volOn ? VOL_BUY : 0;
      var tot = M.purchase + volCost + oneTime;
      var addOns = volCost + oneTime;
      o.price = {
        label: 'Total à la commande', big: EUR0(tot), unit: 'TTC',
        sub: addOns ? 'dont ' + EUR(M.purchase) + ' de prix d’achat + ' + EUR(addOns) + (volOn && oneTime ? ' d’options et d’extras' : (volOn ? ' de couverture contre le vol' : ' d’extras')) : 'Prix d’achat comptant',
        terms: volOn ? TEXT.volBuy : (is360 ? 'Garantie 2 ans, 5 ans sur le cadre aluminium.' : '')
      };
      o.recap.push(row('Prix d’achat', EUR(M.purchase)));
      if (volOn) o.recap.push(row('Couverture contre le vol (24 mois)', '+ ' + EUR(VOL_BUY)));
      o.recap = o.recap.concat(oneTimeRows());
      o.recap.push(row('Total à la commande', EUR(tot), true));
      o.total = { label: 'Total à la commande', value: EUR(tot), unit: '' };
      if (volOn) o.extras.push('dont couverture contre le vol 70,80 € (24 mois)');
    } else {
      var f = M.fin(st.vol);
      var vehicleOnly = volOn && !f.withVol;   /* Ultra + vol : mensualité non affichée par Augment */
      var terms = [];
      if (vehicleOnly) terms.push(TEXT.volFin);
      if (oneTime) terms.push('Extras ' + EUR(oneTime) + ' non inclus dans l’exemple de crédit.');
      o.price = {
        label: vehicleOnly ? 'Financement PayPal (véhicule seul)' : 'Financement PayPal',
        big: EUR(f.monthly), unit: '/ mois',
        sub: f.months + ' · TAEG fixe 15,99 % · montant total dû ' + EUR(f.total) + (f.withVol ? ' · couverture contre le vol incluse' : ''),
        terms: terms.join(' ')
      };
      var totLabel = oneTime ? 'Montant total dû, véhicule seul (exemple PayPal)' : 'Montant total dû';
      o.recap.push(row('Mensualité', EUR(f.monthly)));
      o.recap.push(row('Durée', f.months));
      o.recap.push(row('TAEG fixe', '15,99 %'));
      o.recap.push(row(totLabel, EUR(f.total), true));
      if (f.withVol) o.recap.push(row('Dont couverture contre le vol', EUR(VOL_BUY)));
      else if (vehicleOnly) o.recap.push(row('Couverture contre le vol', 'Non relevée'));
      o.recap = o.recap.concat(oneTimeRows());
      if (oneTime) o.recap.push(row('Extras hors exemple de crédit', '+ ' + EUR(oneTime)));
      o.total = { label: totLabel, value: EUR(f.total), unit: '' };
      o.extras.push(f.months + ' · TAEG fixe 15,99 %');
      if (oneTime) o.extras.push('extras + ' + EUR(oneTime) + ' non inclus dans l’exemple de crédit');
      o.credit = 'Exemple : ' + EUR(f.monthly) + ' / mois sur ' + f.months + ', TAEG fixe 15,99 %, montant total dû ' + EUR(f.total) + '.' + (is360 ? ' ' + TEXT.fin360 : '');
    }

    var opt = function (key, label, sub, price) { return { key: key, label: label, sub: sub, price: price, checked: !!st[key] }; };
    o.options = [];
    if (M.agaru) {
      var volPrice = mode === 'sub' ? '+2,95 €/mois' : '+70,80 €';
      o.options.push(opt('vol', 'Couverture contre le vol', 'Vol, vandalisme et perte. Choisie par 71 % des clients. Franchise 100 € sans batterie, 150 € avec batterie.', volPrice));
      o.options.push(opt('signals', 'Clignotants Agaru', 'Extra proposé au tunnel de commande.', 'Gratuit'));
    }
    o.options.push(opt('helmet', 'Casque Alpina Soho', mode === 'sub' ? 'Il est à vous à la fin du contrat. Taille S : 1,62 €/mois, M/L : 1,65 €/mois.' : 'Taille à choisir sur augment.eco.', mode === 'sub' ? '+1,62 €/mois' : '+39,00 €'));
    if (is360) o.options.push(opt('battery', '2e batterie 1 080 Wh', '+50 km : porte l’autonomie à 106 km.', '+690,00 €'));

    o.service = !M.agaru ? TEXT.service360 : (M.key === 'smart' ? TEXT.serviceSmart : (mode === 'sub' ? TEXT.serviceUltraSub : TEXT.serviceUltraBuy));
    return o;
  }

  /* ==========================================================================
     Lien vers le tunnel de commande augment.eco, pré-rempli avec la configuration.
     Paramètres relevés sur augment.eco/fr-fr/checkout/configure le 07/11/2026.
     La durée, l'acompte et la taille du casque ne passent pas par l'adresse :
     ils se règlent sur la page d'Augment. Le lien passe par AWIN (lien profond autorisé).
     ========================================================================== */
  var CHECKOUT = {
    smart: { name: 'agaru-smart', addons: 'Agaru-499-Wh-Battery,Speed-25kmh' },
    ultra: { name: 'agaru-ultra', addons: 'Agaru-768-Wh-Battery' },
    '360': { name: 'augment-360', addons: '360-1080-Wh-Battery,Speed-45kmh' }
  };
  function checkoutUrl(st, mode) {
    var M = MODELS[st.model], C = CHECKOUT[st.model], sub = mode === 'sub';
    var services = [], accessories = [];
    if (M.agaru) {
      if (sub) services.push('E-Scooter-All-Inclusive-Maintenance');
      if (st.vol) services.push('Theft-coverage');
      if (st.signals) accessories.push(sub ? 'Agaru-Turning-Signals-RECURRING-0' : 'Agaru-Turning-Signals-Charge-ONE_TIME-0');
    } else if (st.battery) {
      accessories.push('360-1080-Wh-Battery-Extra-Charge-ONE_TIME-69000');
    }
    var url = 'https://augment.eco/fr-fr/checkout/configure?scooterName=' + C.name +
      '&mode=' + (sub ? 'subscription' : 'purchase') +
      '&addonIds=' + encodeURIComponent(C.addons) +
      '&serviceIds=' + encodeURIComponent(services.join(',')) +
      '&accessoryIds=' + encodeURIComponent(accessories.join(','));
    return 'https://www.awin1.com/cread.php?awinmid=131358&awinaffid=3099440&ued=' + encodeURIComponent(url) + '&platform=pl';
  }
  function checkoutHint(st, mode) {
    var todo = [];
    if (mode === 'sub') todo.push('durée ' + st.dur + ' mois et acompte de ' + EUR0(MODELS[st.model].sub.acomptes[st.ac]));
    if (mode === 'fin') todo.push('paiement en plusieurs fois (PayPal) à l’étape du paiement');
    if (st.helmet) todo.push('ajout du casque avec sa taille');
    return 'Modèle et options déjà cochés sur augment.eco.' + (todo.length ? ' Il vous restera à choisir : ' + todo.join(' ; ') + '.' : '');
  }

  /* Exposé pour les tests automatisés uniquement. */
  window.__AE_CONFIG = { MODELS: MODELS, computeOffer: computeOffer, checkoutUrl: checkoutUrl, fr: fr };

  /* ==========================================================================
     Interface
     ========================================================================== */
  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var sim = $('[data-sim]');
  if (!sim) return;

  var initial = 'ultra';
  try { var q = new URLSearchParams(window.location.search).get('model'); if (q && MODELS[q]) initial = q; } catch (e) { /* URL non lisible */ }
  var state = {
    model: initial, mode: initial === 'smart' ? 'buy' : 'sub', view: 0,
    dur: 36, ac: 0, vol: true, signals: false, helmet: false, battery: false
  };
  var hot = { open: null, pinned: false };

  function M() { return MODELS[state.model]; }
  function views() { return M().agaru ? AGARU_VIEWS : S360_VIEWS; }
  function points() { return M().agaru ? agaruPoints(M()) : S360_POINTS; }
  function setText(sel, s) { var el = $(sel); if (el) el.textContent = fr(s); }
  function show(sel, on) { var el = $(sel); if (el) el.hidden = !on; }

  /* ---------- Modèle ---------- */
  function selectModel(key) {
    if (!MODELS[key] || key === state.model) return;
    var wasAgaru = M().agaru;
    state.model = key;
    if (key === 'smart' && state.mode === 'sub') state.mode = 'buy';
    if (key !== '360') state.battery = false;
    if (wasAgaru !== M().agaru) state.view = 0;
    closeBubble();
    try {
      var u = new URL(window.location.href);
      u.searchParams.set('model', key);
      window.history.replaceState(null, '', u.toString());
    } catch (e) { /* historique indisponible */ }
    render();
  }

  /* ---------- Scène produit ---------- */
  var stage = $('[data-stage]'), frame = $('[data-frame]'), mainImg = $('[data-main-img]');
  /* Fond flou des vues « studio » : la même image agrandie et floutée, pour que la photo 3:2 remplisse la scène carrée sans bandes. */
  var blurEl = document.createElement('div'); blurEl.className = 'viewer__blur'; blurEl.setAttribute('aria-hidden', 'true'); stage.insertBefore(blurEl, stage.firstChild);
  var hotspots = $('[data-hotspots]'), viewsBox = $('[data-views]'), bubble = $('[data-bubble]');
  var family = null;

  /* srcset d'une vue : sans lui, le srcset de la balise d'origine l'emportait sur le src et la galerie restait sur la
     première image. Détourés : -800, -1280 et pleine taille ; photos : -800 et pleine taille. */
  function srcsetOf(v) {
    var b = v.src.replace(/\.webp$/, '');
    return (v.photo || v.studio) ? b + '-800.webp 800w, ' + v.src + ' ' + v.w + 'w'
                   : b + '-800.webp 800w, ' + b + '-1280.webp 1280w, ' + v.src + ' ' + v.w + 'w';
  }

  /* Libellé affiché d'une vue, sans répéter « Vue » (ex. « Vue 3/4 dépliée » → « 3/4 dépliée »). */
  function vlabel(v) { return v.label.replace(/^Vue\s+/, ''); }

  function renderViews() {
    var V = views(), fam = M().agaru ? 'agaru' : '360';
    if (fam !== family) {
      family = fam;
      viewsBox.innerHTML = V.map(function (v, i) {
        return '<button type="button" class="view' + ((v.photo || v.studio) ? ' view--photo' : '') + '" data-view="' + i + '" aria-pressed="false" ' +
          'aria-label="' + esc('Image ' + (i + 1) + ' sur ' + V.length + ' : ' + vlabel(v)) + '">' +
          '<span class="view__img"><img src="' + v.src.replace(/\.webp$/, '-800.webp') + '" width="' + v.w + '" height="' + v.h + '" alt="" decoding="async"></span></button>';
      }).join('');
    }
    $$('.view', viewsBox).forEach(function (b, i) { b.setAttribute('aria-pressed', String(i === state.view)); });
  }

  function renderStage() {
    var V = views()[state.view], m = M();
    frame.style.setProperty('--r', V.w + ' / ' + V.h);
    frame.classList.toggle('is-posed', !!V.posed);
    frame.classList.toggle('is-photo', !!V.photo);
    frame.classList.toggle('is-studio', !!V.studio);
    stage.classList.toggle('is-studio', !!V.studio);
    blurEl.style.backgroundImage = V.studio ? 'url(' + V.src.replace(/\.webp$/, '-800.webp') + ')' : '';
    stage.classList.toggle('is-photo', !!V.photo);
    frame.classList.toggle('is-main', !!V.main);
    if (mainImg.getAttribute('src') !== V.src) {
      frame.classList.add('is-swapping');
      mainImg.onload = function () { frame.classList.remove('is-swapping'); };
      mainImg.setAttribute('width', V.w);
      mainImg.setAttribute('height', V.h);
      mainImg.sizes = V.photo ? '(max-width: 959px) 144vw, 1110px' : V.studio ? '(max-width: 959px) 96vw, 740px' : '(max-width: 959px) 92vw, 740px';
      mainImg.srcset = srcsetOf(V);
      mainImg.src = V.src;
      setTimeout(function () { frame.classList.remove('is-swapping'); }, 600);
    }
    mainImg.alt = fr(V.alt);
    setText('[data-view-tag]', (state.view + 1) + ' / ' + views().length);
    var cap = $('[data-caption]');
    cap.innerHTML = '<span>' + t(V.main ? 'Survolez ou touchez les points numérotés pour découvrir les 4 points clés.' : V.caption) + '</span>';
    hotspots.innerHTML = V.main ? points().map(function (p, i) {
      return '<button type="button" class="hotspot" data-hot="' + i + '" style="left:' + p.x + '%;top:' + p.y + '%" ' +
        'aria-expanded="false" aria-controls="bubble" aria-describedby="hs-d' + i + '" aria-label="Point ' + p.n + NB + ': ' + t(p.title) + '"><span>' + p.n + '</span></button>' +
        '<span class="sr-only" id="hs-d' + i + '" hidden>' + t(p.text) + '</span>';
    }).join('') : '';
    renderViews();
  }

  function setView(i) {
    if (i === state.view) return;
    state.view = i;
    closeBubble();
    renderStage();
    renderPoints();
  }

  /* ---------- Points chauds + bulle ---------- */
  function openBubble(i, pinned) {
    var P = points()[i], btn = $('[data-hot="' + i + '"]', hotspots);
    if (!P || !btn) return;
    hot.open = i; hot.pinned = !!pinned;
    $('[data-bubble-n]').textContent = P.n;
    $('[data-bubble-t]').textContent = fr(P.title);
    $('[data-bubble-x]').textContent = fr(P.text);
    bubble.hidden = false;
    var s = stage.getBoundingClientRect(), b = btn.getBoundingClientRect();
    var cx = b.left + b.width / 2 - s.left, cy = b.top + b.height / 2 - s.top;
    var bw = bubble.offsetWidth, bh = bubble.offsetHeight, pad = 12;
    var left = Math.max(pad, Math.min(cx - bw / 2, s.width - bw - pad));
    var above = cy > s.height * 0.5;
    var top = above ? cy - 28 - bh : cy + 28;
    top = Math.max(pad, Math.min(top, s.height - bh - pad));
    bubble.style.left = left + 'px';
    bubble.style.top = top + 'px';
    bubble.classList.toggle('is-above', above);
    syncHot();
  }
  function closeBubble() {
    hot.open = null; hot.pinned = false;
    if (bubble) bubble.hidden = true;
    syncHot();
  }
  function syncHot() {
    $$('.hotspot', hotspots).forEach(function (h, i) {
      var on = hot.open === i;
      h.classList.toggle('is-active', on);
      h.setAttribute('aria-expanded', String(on));
    });
    $$('.point', $('[data-points]')).forEach(function (p, i) { p.classList.toggle('is-active', hot.open === i); });
  }

  hotspots.addEventListener('pointerenter', function (e) {
    var h = e.target.closest && e.target.closest('.hotspot');
    if (h && e.pointerType === 'mouse' && !hot.pinned) openBubble(+h.dataset.hot, false);
  }, true);
  hotspots.addEventListener('pointerleave', function (e) {
    var h = e.target.closest && e.target.closest('.hotspot');
    if (h && e.pointerType === 'mouse' && !hot.pinned && hot.open === +h.dataset.hot) closeBubble();
  }, true);
  hotspots.addEventListener('focusin', function (e) {
    var h = e.target.closest('.hotspot');
    if (h && hot.open !== +h.dataset.hot) openBubble(+h.dataset.hot, false);
  });
  hotspots.addEventListener('focusout', function (e) {
    if (!e.relatedTarget || !e.relatedTarget.closest || !e.relatedTarget.closest('.hotspot')) closeBubble();
  });
  hotspots.addEventListener('click', function (e) {
    var h = e.target.closest('.hotspot');
    if (!h) return;
    var i = +h.dataset.hot;
    if (hot.open === i && hot.pinned) closeBubble(); else openBubble(i, true);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && hot.open !== null) closeBubble();
  });
  document.addEventListener('click', function (e) {
    if (hot.open !== null && !e.target.closest('.hotspot, .bubble, .point')) closeBubble();
  });
  window.addEventListener('resize', function () { if (hot.open !== null) openBubble(hot.open, hot.pinned); });

  viewsBox.addEventListener('click', function (e) {
    var b = e.target.closest('.view');
    if (b) setView(+b.dataset.view);
  });

  /* Galerie : flèches, clavier et glissement au doigt. */
  function stepView(d) { var n = views().length; setView((state.view + d + n) % n); }
  $('[data-view-prev]').addEventListener('click', function () { stepView(-1); });
  $('[data-view-next]').addEventListener('click', function () { stepView(1); });
  stage.addEventListener('keydown', function (e) {
    if (e.target.closest('.hotspot')) return;
    if (e.key === 'ArrowLeft') { e.preventDefault(); stepView(-1); }
    else if (e.key === 'ArrowRight') { e.preventDefault(); stepView(1); }
  });
  var swipeX = null, swipeY = null;
  stage.addEventListener('touchstart', function (e) {
    if (e.target.closest('.hotspot, .viewer__nav')) { swipeX = null; return; }
    swipeX = e.touches[0].clientX; swipeY = e.touches[0].clientY;
  }, { passive: true });
  stage.addEventListener('touchend', function (e) {
    if (swipeX === null) return;
    var dx = e.changedTouches[0].clientX - swipeX, dy = e.changedTouches[0].clientY - swipeY;
    swipeX = null;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy) * 1.5) stepView(dx < 0 ? 1 : -1);
  }, { passive: true });

  /* ---------- Liste des 4 points clés ---------- */
  var pointsBox = $('[data-points]');
  function renderPoints() {
    pointsBox.innerHTML = points().map(function (p, i) {
      return '<li><button type="button" class="point" data-goto="' + i + '">' +
        '<span class="point__n">' + p.n + '</span><span class="point__body"><span class="point__t">' + t(p.title) + '</span>' +
        '<span class="point__x">' + t(p.text) + '</span></span></button></li>';
    }).join('');
    syncHot();
  }
  pointsBox.addEventListener('click', function (e) {
    var b = e.target.closest('.point');
    if (!b) return;
    var i = +b.dataset.goto;
    setView(0);
    var r = stage.getBoundingClientRect();
    if (r.top < 72 || r.bottom > window.innerHeight) stage.scrollIntoView({ block: 'center', behavior: 'smooth' });
    setTimeout(function () { openBubble(i, true); }, r.top < 72 || r.bottom > window.innerHeight ? 450 : 0);
  });
  pointsBox.addEventListener('pointerover', function (e) {
    var b = e.target.closest('.point');
    $$('.hotspot', hotspots).forEach(function (h, i) { h.classList.toggle('is-hint', !!b && +b.dataset.goto === i); });
  });
  pointsBox.addEventListener('pointerleave', function () {
    $$('.hotspot', hotspots).forEach(function (h) { h.classList.remove('is-hint'); });
  });

  /* ---------- Simulateur ---------- */
  var optsBox = $('[data-options]');
  var optsKey = '';

  function renderSim() {
    var m = M(), o = computeOffer(state);
    state.mode = o.mode;
    setText('[data-sim-model]', m.name);

    var subRadio = $('#mode-sub');
    subRadio.disabled = !m.sub;
    $('#mode-' + o.mode).checked = true;
    show('[data-smart-note]', !m.sub);
    setText('[data-smart-note]', TEXT.smartNote);

    setText('[data-price-label]', o.price.label);
    setText('[data-price-big]', o.price.big);
    setText('[data-price-unit]', o.price.unit);
    setText('[data-price-sub]', o.price.sub);
    setText('[data-price-terms]', o.price.terms || '');
    show('[data-price-terms]', !!o.price.terms);

    var cta = $('[data-cta]');
    if (cta) cta.href = checkoutUrl(state, o.mode);
    setText('[data-cta-hint]', checkoutHint(state, o.mode));

    show('[data-subctl]', !!o.sub);
    if (o.sub) {
      $('#dur-' + o.sub.dur).checked = true;
      $('#ac-' + o.sub.ac).checked = true;
      o.sub.acomptes.forEach(function (a, i) { setText('label[for="ac-' + i + '"]', EUR0(a)); });
      /* Économie : pastille seulement si elle est réelle ; sinon une simple incitation (pas de « 0,00 € »). */
      var sv = $('[data-saving]');
      sv.innerHTML = o.sub.saving
        ? '<span class="saving__k">Économie totale sur ' + o.sub.dur + '&nbsp;mois</span><b>' + EUR(o.sub.saving) + '</b>'
        : '<span class="saving__k">' + t('Acompte max. sur ' + o.sub.dur + ' mois : ' + EUR(o.sub.savingMax) + ' d’économie totale') + '</span>';
      sv.classList.toggle('is-on', !!o.sub.saving);
    }

    /* Options : reconstruites seulement si la liste change (garde le focus clavier). */
    var key = state.model + '|' + o.mode;
    if (key !== optsKey) {
      optsKey = key;
      optsBox.innerHTML = o.options.map(function (op) {
        var id = 'opt-' + op.key;
        return '<li class="opt"><label class="opt__row" for="' + id + '">' +
          '<span class="opt__txt"><span class="opt__name">' + t(op.label) + '</span><span class="opt__sub" data-opt-sub="' + op.key + '">' + t(op.sub) + '</span></span>' +
          '<span class="opt__price">' + t(op.price) + '</span>' +
          '<input class="toggle" type="checkbox" id="' + id + '" data-opt="' + op.key + '"' + (op.checked ? ' checked' : '') + '>' +
          '</label></li>';
      }).join('');
    } else {
      o.options.forEach(function (op) { var c = $('#opt-' + op.key); if (c) c.checked = op.checked; });
    }
    show('[data-vol360]', m.key === '360');
    setText('[data-vol360]', TEXT.vol360);

    setText('[data-total-label]', o.total.label);
    setText('[data-total-value]', o.total.value);
    setText('[data-total-unit]', o.total.unit);
    $('[data-total-unit]').hidden = !o.total.unit;
    setText('[data-total-extra]', o.extras.join(' · '));
    $('[data-total-extra]').hidden = !o.extras.length;
    $('[data-recap]').innerHTML = o.recap.map(function (r) {
      return '<div class="recap__row' + (r.strong ? ' is-strong' : '') + '"><dt>' + t(r.label) + '</dt><dd>' + t(r.value) + '</dd></div>';
    }).join('');

    show('[data-credit]', !!o.credit);
    if (o.credit) setText('[data-credit-text]', o.credit + ' ' + TEXT.creditMore);
    var svc = $('[data-service]');
    svc.classList.toggle('is-360', !m.agaru);
    svc.innerHTML = (m.agaru ? ICON.shield : ICON.info) + '<span>' + t(o.service) + '</span>';
    updateStick();
  }

  var ICON = {
    shield: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
    info: '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><path d="M12 7.5v.01"/></svg>'
  };

  sim.addEventListener('submit', function (e) { e.preventDefault(); });
  sim.addEventListener('change', function (e) {
    var el = e.target;
    if (el.name === 'mode') state.mode = el.value;
    else if (el.name === 'dur') state.dur = +el.value;
    else if (el.name === 'ac') state.ac = +el.value;
    else if (el.dataset.opt) state[el.dataset.opt] = el.checked;
    else return;
    renderSim();
  });

  /* Carte collante : si elle dépasse la hauteur de l'écran, elle défile puis se cale en bas. */
  var wide = window.matchMedia('(min-width: 960px)');
  function updateStick() {
    if (!wide.matches) { sim.style.removeProperty('--stick-top'); return; }
    var top = Math.min(96, window.innerHeight - sim.offsetHeight - 16);
    sim.style.setProperty('--stick-top', top + 'px');
  }
  window.addEventListener('resize', updateStick);
  $$('details', sim).forEach(function (d) { d.addEventListener('toggle', updateStick); });

  /* ---------- L'essentiel ---------- */
  function renderEss() {
    var m = M();
    setText('[data-ess-name]', m.name);
    setText('[data-ess-lead]', m.agaru
      ? 'Agaru Smart et Agaru Ultra partagent le même moteur, les mêmes freins, les mêmes pneus et la même étanchéité. Seuls la batterie et le poids diffèrent.'
      : 'Scooter à assise, catégorie L1e (cyclomoteur), 45 km/h. Garantie 2 ans, 5 ans sur le cadre aluminium ; pièces d’usure disponibles, réparation tout compris non incluse.');
    $('[data-stats]').innerHTML = m.stats.map(function (s) {
      return '<div class="stat"><span class="label">' + t(s[0]) + '</span><b class="stat__v">' + t(s[1]) + '<small>' + t(s[2]) + '</small></b>' +
        (s[3] ? '<span class="stat__sub">' + t(s[3]) + '</span>' : '') + '</div>';
    }).join('');
    var map = {};
    m.specs.forEach(function (s) { map[s[0]] = s[1]; });
    $('[data-specs]').innerHTML = SPEC_GROUPS.map(function (g) {
      var rows = g[1].filter(function (k) { return map[k] !== undefined; });
      if (!rows.length) return '';
      return '<div class="specs__group"><h3 class="specs__gt">' + t(g[0]) + '</h3><dl class="specs__dl">' + rows.map(function (k) {
        return '<div><dt>' + t(k) + '</dt><dd>' + t(map[k]) + '</dd></div>';
      }).join('') + '</dl></div>';
    }).join('');
    setText('[data-specs-meta]', m.specs.length + ' caractéristiques');
    $('[data-equip]').innerHTML = m.equip.map(function (e) { return '<li>' + t(e) + '</li>'; }).join('');
    setText('[data-quote]', m.quote);
    setText('[data-app-text]', m.agaru ? TEXT.appAgaru : TEXT.app360);
    setText('[data-app-model]', m.name);
    var img = $('[data-app-img]'), src = m.agaru ? 'img/augment-app.webp' : 'img/360-app.webp';
    if (img.getAttribute('src') !== src) {
      img.src = src;
      img.setAttribute('width', m.agaru ? 1274 : 1273);
      img.alt = m.agaru ? 'Application mobile Augment sur smartphone' : 'Application mobile Augment pour l’E-scooter 360 sur smartphone';
    }
  }

  /* ---------- Rendu global ---------- */
  function render() {
    $$('input[name="model"]').forEach(function (r) { r.checked = r.value === state.model; });
    renderStage();
    renderPoints();
    renderSim();
    renderEss();
  }
  $('[data-models]').addEventListener('change', function (e) {
    if (e.target.name === 'model') selectModel(e.target.value);
  });

  render();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(updateStick);
  window.addEventListener('load', updateStick);
})();
