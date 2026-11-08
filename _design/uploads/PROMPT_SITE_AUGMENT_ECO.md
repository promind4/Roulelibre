# CAHIER DES CHARGES & PROMPTS SYSTÈME — SITE D'AFFILIATION AUGMENT ECO
## Référentiel corrigé à 100 % sur la base du relevé officiel `augment.eco` & `help.augment.eco/fr` (07/11/2026)

---

## 0. RÈGLES D'OR & GARDE-FOUS FACTUELS (À FOURNIR IMPÉRATIVEMENT AU MODÈLE)

1. **Aucune donnée inventée :** Seules les caractéristiques, tarifs et conditions figurant dans ce document (et dans `D:\AUGMENT_ECO_REFERENCE_TECHNIQUE.md`) peuvent être affichés.
2. **Trois modèles commercialisés en France (et aucun autre) :**
   * `01. Agaru Smart` (E-trottinette EDPM — 25 km/h — 50 km — Achat 399 € / Financement dès 19,33 €/mois).
   * `02. Agaru Ultra` (E-trottinette EDPM — 25 km/h — 70 km — Achat 549 € / Abonnement de 16,95 € à 44,95 €/mois).
   * `03. E-scooter 360` (Scooter électrique à assise pliable, homologué **catégorie L1e** — 45 km/h — 53 km à 106 km — Achat 1 890 € / Abonnement de 25,90 € à 159,90 €/mois).
   * *Note stricte :* Le modèle historique *Alturo* n'est plus commercialisé en France et ne doit **jamais** apparaître.
3. **Différenciation mécanique exacte :**
   * Les **Agaru Smart et Agaru Ultra sont mécaniquement identiques** (même moteur 500 W / 800 W crête, même couple 26 Nm, même pente 23 %, mêmes pneus 10 × 2,5", même freinage **disque mécanique à l'ARRIÈRE + eABS électronique à l'AVANT**, même étanchéité IPX5), à l'exception de **la capacité de leur batterie fixe intégrée au plateau** (`499 Wh` vs `768 Wh`) et de **leur poids** (`20 kg` vs `20,7 kg`).
   * L'**E-scooter 360** n'est pas une trottinette debout mais un **cyclomoteur électrique pliable à assise (catégorie L1e, 45 km/h)** doté d'un moteur de `2 140 W` (`105 Nm`), d'une ou deux **batteries amovibles de `1 080 Wh`** (`5,2 kg` chacune) sous la selle, de pneus tubeless `120/90-R10` et de **freins à disque hydrauliques**.
4. **Distinction stricte du Service Après-Vente (SAV) :**
   * **Agaru Smart & Ultra :** Bénéficient du service *« Réparations et remplacements gratuits. Tout est couvert »* (trottinettes de rechange, pièces détachées, usure naturelle, accidents, pannes, batterie, freins et pneus inclus — disponible en abonnement ET en option à l'achat).
   * **E-scooter 360 :** **Exception critique** — *« Un service de pièces détachées pour les pièces d'usure est disponible pour le 360, mais le service de réparation tout compris des trottinettes n'est pas inclus. »* Il est couvert par une **garantie de 2 ans (5 ans sur le cadre aluminium)**.
5. **Lien d'affiliation AWIN unique sur tous les boutons d'action (CTA) :**
   * `https://www.awin1.com/awclick.php?mid=131358&id=3099440`

---

## 1. INVENTAIRE DES VISUELS OFFICIELS DISPONIBLES DANS `D:\AUGMENT ECO\`

Tous les visuels officiels téléchargés depuis `augment.eco` sont présents dans `D:\AUGMENT ECO\` aux formats `.avif` et `.png` haute définition :

### Dossier `D:\AUGMENT ECO\AGARU SMART\` (et `AGARU ULTRA\`) :
* `01_agaru_smart_profil_deplie.png` / `01_agaru_ultra_profil_deplie.png` : Profil latéral complet déplié de l'e-trottinette (on distingue clairement le **frein à disque mécanique sur la roue arrière** et le moteur/eABS à l'avant).
* `02_agaru_smart_profil_plie.png` : Vue latérale de la trottinette repliée (potence rabattue, crochet engagé dans le garde-boue arrière).
* `03_agaru_smart_cockpit_ecran_led.png` : Gros plan du guidon élargi, écran LED affichant la vitesse (`20 km/h`), le niveau de batterie, le bouton de fonction et les commandes de clignotants gauche/droite.
* `04_agaru_smart_guidon_clignotants.png` : Vue face avant du guidon avec phare LED central et clignotants intégrés aux extrémités des poignées allumés.
* `05_agaru_smart_plateau_frein_disque_arriere.png` : Gros plan sur le plateau (batterie fixe intégrée), le feu stop arrière et l'étrier de frein à disque mécanique arrière sur pneu `10 × 2,5 pouces`.
* `06_augment_application_mobile.png` : Interface de l'application mobile Augment sur smartphone (curseur de verrouillage antivol digital vert fluo, statistiques de trajet, état batterie).

### Dossier `D:\AUGMENT ECO\E SCOOTER 360\` :
* `01_scooter_360_vue_3_4_deplie.png` : Vue 3/4 avant de l'E-scooter 360 déplié (phare avant intégré, rétroviseur, selle, colonne siglée `augment°`, frein à disque hydraulique avant).
* `02_scooter_360_profil_plie.png` : Profil latéral en position repliée compacte (`1265 × 350 × 1180 mm`).
* `03_scooter_360_selle_ouverte_double_batterie_1080wh.png` : Gros plan de la selle ouverte dévoilant l'emplacement pour **2 batteries amovibles Li-ion 21700 de 1 080 Wh** avec poignées d'extraction.
* `04_scooter_360_roue_arriere_disque_hydraulique_charniere_orange.png` : Gros plan sur la roue arrière `120/90-R10`, le frein à disque hydraulique arrière, le support de plaque L1e et la molette orange de déverrouillage/pliage du bras oscillant.
* `05_augment_application_mobile.png` : Application mobile Augment (modes de conduite et protection antivol bloquant la roue arrière).

---

## 2. PRÉAMBULE DE CONTEXTE GLOBAL (À COPIER EN DÉBUT DE CONVERSATION AVEC CLAUDE / OPENAI)

```markdown
### CONTEXTE SYSTÈME & SOURCE DE VÉRITÉ (PROJET SITE D'AFFILIATION AUGMENT ECO)

1. **Identité réelle de la marque Augment (`augment.eco`) :**
   - Marque **autrichienne** fondée en **2015 à Pinzgau**, issue à l'origine de la fabrication de skis de compétition de Coupe du Monde FIS (`Augment.Ski` — titres olympiques et paralympiques 2022, partenariats avec Van Deer / Red Bull / Marcel Hirscher et Red Bull KTM Ajo MotoGP).
   - Lancement en 2020 de l'offre d'abonnement d'e-trottinettes (en Finlande, Autriche et Suède). Aujourd'hui présente en **France, Finlande, Suède, Danemark, Autriche, Royaume-Uni, Italie, Belgique, Suisse, Espagne et Luxembourg** (plus de 80 collaborateurs).
   - Positionnement officiel : *« La référence européenne du leasing (LOA) d'e-trottinettes »*.

2. **Nature de notre site :**
   - Nous construisons un **site comparatif et guide éditorial indépendant multi-pages** (et non le site officiel de la marque).
   - Bandeau obligatoire en en-tête et pied de page : *« Site comparatif indépendant. Non affilié éditorialement à Augment. Liens partenaires rémunérés. »*
   - Mention obligatoire sous chaque tarif : *« Prix relevés le 07/11/2026 sur augment.eco. Susceptibles de modification — seul le prix affiché sur le site du marchand fait foi. »*
   - Tous les boutons d'action (CTA) pointent vers le lien affilié AWIN : `https://www.awin1.com/awclick.php?mid=131358&id=3099440`

3. **Les 3 seuls véhicules du catalogue France (Données vérifiées au 07/11/2026) :**
   - **01. Agaru Smart** (« Le choix malin » — E-trottinette EDPM) :
     * Moteur `500 W` (`800 W` max) · Couple `26 Nm` · Pente `23 %` · Vitesse max `25 km/h`.
     * Batterie **fixe** intégrée au plateau `10,4 Ah / 499 Wh` Li-ion · Autonomie max `50 km`.
     * Pneus à air `10 × 2,5 pouces` (`10"`) · Poids `20 kg` · Étanchéité `IPX5`.
     * Freinage : **Frein à disque mécanique à l'ARRIÈRE + eABS électronique à l'AVANT**.
     * Équipements : Clignotants, guidon élargi, app mobile, antivol digital, pliage rapide.
     * Tarifs FR : **Achat comptant `399 €`** · **Financement PayPal `19,33 €/mois` sur 24 mois** (TAEG 15,99 %, total 463,78 €). *(Note : l'accroche « 23,95 €/mois avec 23 € d'apport » figure sur le site, mais seul le mode Achat est actuellement ouvert dans le tunnel FR pour le Smart).*
   - **02. Agaru Ultra** (« La meilleure autonomie » — E-trottinette EDPM) :
     * Mécaniquement identique au Smart, mais doté d'une batterie haute capacité **fixe** de **`16 Ah / 768 Wh`** offrant jusqu'à **`70 km` d'autonomie** (« la seule trottinette en leasing privé offrant une autonomie allant jusqu'à 70 km ») pour un poids de **`20,7 kg`**.
     * Tarifs FR :
       - **Achat comptant :** **`549 €`** (Financement PayPal dès `26,59 €/mois` ; `30,02 €/mois` sur 24 mois avec couverture vol, TAEG 15,99 %, total 720,46 €).
       - **Abonnement / Leasing (paliers 12 / 24 / 36 mois) :**
         * 12 mois (acompte min `59 €`) : **`44,95 € / mois`**
         * 24 mois (acompte min `59 €`) : **`32,95 € / mois`**
         * 36 mois (acompte min `59 €`) : **`29,95 € / mois`**
         * 36 mois (acompte max `399 €`) : **`16,95 € / mois`** (économie totale : `128 €`)
   - **03. E-scooter 360** (« Léger. Puissant. Rapide. » — Scooter électrique pliable à assise, **Catégorie L1e**) :
     * Vitesse max **`45 km/h`** · Moteur **`2 140 W`** · Couple **`105 Nm`** · Étanchéité **`IPX4`**.
     * Batterie **amovible** `1 080 Wh` Li-ion 21700 (`5,2 kg` par batterie) sous la selle : autonomie **`53 km` (1 batterie)** ou **`106 km` (2 batteries — batterie supplémentaire en option à `690 €`)**.
     * Poids : **`36 kg` avec batterie (`31 kg` à vide)**.
     * Dimensions : Déplié `1555 × 609 × 1010 mm` · Plié `1265 × 350 × 1180 mm` (se range en intérieur : ascenseur, bureau, appartement).
     * Pneus : **`120/90-R10, 18.5"` tubeless** (compatibles pneus hiver) · **Freins à disque hydrauliques**.
     * Équipements : Démarrage par **badge NFC** sur l'écran, ouverture selle par bouton, verrouillage roue arrière via l'app mobile. Garantie **2 ans (5 ans sur le cadre aluminium)**.
     * Tarifs FR :
       - **Achat comptant :** **`1 890 €`** (Financement PayPal : `91,54 €/mois` sur 24 mois, TAEG 15,99 %, total 2 196,99 €).
       - **Abonnement / Leasing (paliers 12 / 24 / 36 mois) :**
         * 12 mois (acompte min `290 €`) : **`159,90 € / mois`**
         * 24 mois (acompte min `290 €`) : **`89,90 € / mois`**
         * 36 mois (acompte min `290 €`) : **`64,90 € / mois`**
         * 36 mois (acompte max `1 490 €`) : **`25,90 € / mois`** (économie totale : `204 €`)

4. **Règles Esthétiques & Anti-AI-Slop :**
   - Direction artistique industrielle et éditoriale sobre (grille suisse à filets `1px solid #DFDDD6`, fond pierre minérale `#F6F5F0`, cartes `#FFFFFF`, texte noir carbone `#141517`, boutons rectangulaires nets `#1B3B2B`).
   - Zéro émoticône, zéro dégradé néon/violet SaaS, zéro cadre coloré autour du viewport, français irréprochable.
```

---

## 3. LES 3 PROMPTS SYSTÈME POUR GÉNÉRER LES LAYOUTS DESIGN DU SITE COMPLET

### PROMPT N°1 : La Page d'Accueil Globale (Homepage Vitrine Multi-Modèles)

```markdown
Conçois la maquette UI/UX Desktop (plein écran, sans bordure extérieure, style éditorial et industriel scandinave sur fond `#F6F5F0`, grille suisse à filets `1px solid #DFDDD6`, zéro emoji, textes en français exact) pour la **Page d'Accueil Globale** du site comparatif indépendant dédié à Augment Eco.

Structure de la page de haut en bas :
1. **Bandeau supérieur d'indépendance & Header :**
   - Fine barre supérieure : "Site comparatif indépendant • Non affilié éditorialement à Augment • Liens partenaires rémunérés".
   - Barre de navigation : Logo typographique sobre à gauche, liens au centre ("01. La Gamme (Agaru & 360)", "02. Simuler son Forfait", "03. Le Service Tout Couvert", "04. Guides & Réglementation"), sélecteur de pays européens réels (FR / FI / SE / AT / BE / CH / ES / IT) et bouton rectangulaire `#1B3B2B` ("Configurer sur Augment.eco").
2. **Hero Section Asymétrique (Grille 60/40) :**
   - À gauche : Surtitre Monospace "INGÉNIERIE AUTRICHIENNE DEPUIS 2015 • LIVRAISON EN 3-4 JOURS OUVRÉS", titre principal "La référence européenne du leasing d'e-trottinettes et du scooter pliable 360.", sous-titre factuel présentant les 3 modèles en stock (*Agaru Smart* à 399 €, *Agaru Ultra* jusqu'à 70 km dès 16,95 €/mois, et *E-scooter 360* L1e 45 km/h dès 25,90 €/mois). Deux boutons rectangulaires nets ("Comparer les 3 modèles" et "Simuler mon forfait").
   - À droite : Mise en scène studio sobre côte à côte de l'e-trottinette **Agaru Ultra** (`01_agaru_ultra_profil_deplie.png`) et de l'**E-scooter 360** (`01_scooter_360_vue_3_4_deplie.png`).
3. **Vue Synoptique des 3 Véhicules Commercialisés en France (3 grandes cartes techniques alignées) :**
   - Carte 01 : **Agaru Smart** (« Le choix malin » — 50 km, 499 Wh fixe, 20 kg, 500W/800W, Achat 399 € ou Financement 19,33 €/mois).
   - Carte 02 : **Agaru Ultra** (« La meilleure autonomie » — 70 km, 768 Wh fixe, 20,7 kg, 500W/800W, Abonnement de 16,95 € à 44,95 €/mois ou Achat 549 €).
   - Carte 03 : **E-scooter 360** (« Léger. Puissant. Rapide. » — Catégorie L1e, 45 km/h, 2140 W, 105 Nm, 53 à 106 km, batterie amovible 1080 Wh, 36 kg, Abonnement de 25,90 € à 159,90 €/mois ou Achat 1 890 €).
4. **Section « Le Service Sans Stress » (Avec distinction claire Agaru vs 360) :**
   - Colonne Gauche (Agaru Smart & Ultra) : *« Réparations et remplacements gratuits. Tout est couvert »* (Trottinettes de rechange et pièces détachées, usure naturelle, accidents et pannes, batterie/freins/pneus inclus — disponible en abonnement et même à l'achat) + Option *Couverture contre le vol* à 2,95 €/mois (adoptée par 71 % des clients, franchise 100 €/150 €).
   - Colonne Droite (Spécificité E-scooter 360) : Encadré transparent précisant que le 360 dispose d'un service de pièces détachées pour l'usure et d'une **garantie constructeur de 2 ans (5 ans sur le cadre aluminium)**.
5. **Parcours Officiel en 4 Étapes (« Comment s'abonner — En moins de 5 minutes ») :**
   - `01. Sélectionnez votre produit` -> `02. Créez votre forfait (Durée 12/24/36 mois & Acompte)` -> `03. Ajoutez des options (Clignotants gratuits, Casque Alpina Soho 39 €, Couverture vol)` -> `04. Payez en toute sécurité`.
```

---

### PROMPT N°2 : La Fiche Produit & Configurateur Technique (Inspiré du Technical Configurator validé)

```markdown
Conçois la maquette UI/UX Desktop (plein écran, fond `#F6F5F0`, grille technique à filets `1px solid #DFDDD6`, style Braun / Porsche Configurator, zéro emoji, français exact) pour la **Page Fiche Produit & Configurateur Technique** du site.

L'interface s'organise en 3 colonnes sous l'en-tête :
1. **Colonne Gauche — Sélecteur des 3 Modèles Officiels :**
   - `01. Agaru Smart` (« Le choix malin » — EDPM 25 km/h) : Grille 2x2 Monospace (`Poids : 20,0 kg` | `Autonomie : 50 km` | `Batterie : 499 Wh fixe` | `Moteur : 500W / 800W`).
   - `02. Agaru Ultra` (« La meilleure autonomie » — EDPM 25 km/h) : Grille 2x2 Monospace (`Poids : 20,7 kg` | `Autonomie : 70 km` | `Batterie : 768 Wh fixe` | `Moteur : 500W / 800W`).
   - `03. E-scooter 360` (« Léger. Puissant. Rapide. » — Catégorie L1e 45 km/h) : Grille 2x2 Monospace (`Poids : 36 kg (31 kg vide)` | `Autonomie : 53 / 106 km` | `Batterie : 1080 Wh amovible` | `Moteur : 2140 W (105 Nm)`).
2. **Colonne Centrale — Scène Produit sur Socle Béton & Lignes de Cotation Exactes :**
   - Affiche le véhicule sélectionné posé sur un socle en béton brut (avec sélecteur de vue permettant de basculer entre les photos officielles : *Profil déplié*, *Profil plié*, *Cockpit LED / Selle ouverte*, *Détail frein arrière*).
   - **Si Agaru Smart ou Ultra est sélectionné**, les 4 lignes de cotation pointent exactement sur :
     1. *Guidon élargi & Écran LED :* Clignotants intégrés aux poignées (option gratuite), bouton multifonction et verrouillage via application mobile.
     2. *Plateau central :* Batterie Li-ion fixe intégrée au plateau (`499 Wh` sur Smart / `768 Wh` sur Ultra), étanchéité `IPX5`.
     3. *Roue avant :* Moteur `500 W` (`800 W` crête, couple `26 Nm`, pentes `23 %`) + **Freinage électronique eABS à l'avant**.
     4. *Roue arrière :* Pneus à air `10 × 2,5 pouces` + **Frein à disque mécanique à l'arrière**.
   - **Si E-scooter 360 est sélectionné**, les 4 lignes de cotation pointent exactement sur :
     1. *Selle à ouverture par bouton & Écran NFC :* Démarrage sans clé par badge NFC + logement pour 1 ou 2 batteries amovibles `1 080 Wh` (`5,2 kg` l'unité, jusqu'à 106 km).
     2. *Charnière centrale à molette orange :* Pliage compact (`1265 × 350 × 1180 mm`) pour rangement en appartement, ascenseur ou bureau. Cadre aluminium garanti 5 ans.
     3. *Roue arrière :* Moteur `2 140 W` à fort couple (`105 Nm`, vitesse `45 km/h` L1e) avec blocage antivol de la roue arrière via l'application.
     4. *Trains roulants :* Pneus larges tubeless `120/90-R10 (18.5")` compatibles pneus hiver + **Freins à disque hydrauliques**.
3. **Colonne Droite — Simulateur Officiel à Double Curseur (Abonnement vs Achat vs Financement) :**
   - Onglets en haut du panneau : `Abonnement (LOA)` | `Achat Comptant` | `Financement PayPal 24 mois`.
   - **Deux curseurs interactifs fidèles au tunnel Augment :**
     - Curseur 1 : **Durée minimale** (`12 mois` · `24 mois` · `36 mois`).
     - Curseur 2 : **Acompte initial** (pour Agaru Ultra : de `59 €` à `399 €` -> mensualité de `44,95 €` à `16,95 €/mois` ; pour E-scooter 360 : de `290 €` à `1 490 €` -> mensualité de `159,90 €` à `25,90 €/mois`).
   - Cases d'options officielles :
     - `[x] Couverture contre le vol (+2,95 €/mois — choisie par 71 % des clients)` (pour Agaru).
     - `[ ] Clignotants Agaru (0,00 € — Gratuit)` / `[ ] Casque Alpina Soho (+39,00 €)` / `[ ] 2e Batterie 1080 Wh pour 360 (+690,00 €)`.
   - Bouton CTA rectangulaire vert pin `#1B3B2B` pleine largeur : `Configurer cette offre sur Augment.eco ->` (avec mention légale : *"Prix relevés le 07/11/2026 sur augment.eco"*).
```

---

### PROMPT N°3 : Le Comparateur Détaillé & Hub Éditorial SEO (Guides, Réglementation & Entreprises)

```markdown
Conçois la maquette UI/UX Desktop (plein écran, fond `#F6F5F0`, grille suisse `1px`, style magazine technique scandinave, zéro emoji, français exact) pour la **Page Comparateur & Hub de Guides SEO**.

Structure de l'écran en 3 sections :
1. **Section 1 — Le Grand Tableau Comparatif Technique & Tarifaire (Agaru Smart vs Agaru Ultra vs E-scooter 360) :**
   - Tableau d'ingénierie complet alignant les 14 critères officiels vérifiés : Catégorie (`EDPM` vs `L1e`), Vitesse max (`25 km/h` vs `45 km/h`), Autonomie max (`50 km` vs `70 km` vs `53/106 km`), Batterie (`499 Wh fixe` vs `768 Wh fixe` vs `1080 Wh amovible`), Moteur (`500 W` vs `2140 W`), Couple (`26 Nm` vs `105 Nm`), Poids (`20 kg` vs `20,7 kg` vs `36 kg`), Freinage (`Disque AR + eABS AV` vs `Disques hydrauliques`), Étanchéité (`IPX5` vs `IPX4`), Service inclus (`Réparations & remplacement tout compris` vs `Garantie 2 ans / 5 ans cadre alu`), Prix achat (`399 €` / `549 €` / `1 890 €`) et Mensualités.
2. **Section 2 — Espace Entreprises / Flottes & Cadre Réglementaire Français :**
   - Carte Gauche (Fond contraste `#141517`, texte clair) : **Offre Entreprises & Mobilité Salariés** (*« Moderniser votre entreprise ? Déplacer vos équipes ou offrir la micromobilité à vos clients »*) + point informatif sur les dispositifs de prise en charge employeur et l'obligation d'assurance Responsabilité Civile EDPM / immatriculation L1e.
   - Carte Droite : **Synthèse des Avis Clients Vérifiés (Source Trustpilot)** résumant les retours sur le rapport qualité-prix, la prise en charge de la maintenance, la livraison en 3-4 jours ouvrés et l'application mobile.
3. **Section 3 — Maillage des Guides Pratiques SEO & FAQ Issue du Centre d'Aide (`help.augment.eco`) :**
   - Grille de 4 guides éditoriaux :
     - *Guide 01 :* "Agaru Smart vs Agaru Ultra : les 768 Wh valent-ils l'écart de prix ?"
     - *Guide 02 :* "Augment 360 (Catégorie L1e) : assurance, immatriculation et rangement en appartement"
     - *Guide 03 :* "Comment fonctionne concrètement la garantie 'Tout est couvert' et la couverture vol à 2,95 €/mois ?"
     - *Guide 04 :* "Entretien, pression des pneus à froid et bonnes pratiques de charge de la batterie Li-ion"
   - Accordéon FAQ technique (bouton multifonction 1 à 6 appuis, pliage du guidon, franchises vol 100 €/150 €, délais de livraison 3-4 jours ouvrés) + Pied de page complet avec mentions légales, politique cookies CNIL et déclaration d'affiliation AWIN.
```
