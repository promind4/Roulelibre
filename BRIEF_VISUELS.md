# Brief visuels — Guide Augment Eco

Images à générer (OpenAI ou autre modèle) pour illustrer le site. Les prompts sont en anglais, car les générateurs le comprennent mieux.

## Règles communes

- **Produits fidèles** : partir des photos détourées de `site/img/` (image de référence ou « image-to-image ») pour garder le vrai design : cadre, guidon, roues, batterie. Une image qui montre un produit différent du vrai, ou une caractéristique qu'il n'a pas, serait trompeuse.
- **Usage réaliste** :
  - Agaru : une seule personne, sur une piste cyclable ou en ville, casque conseillé.
  - E-scooter 360 (cyclomoteur L1e) : **casque et gants obligatoires**, plaque d'immatriculation à l'arrière, sur la chaussée et non sur le trottoir.
- **Pas de texte ni de logo inventé** dans l'image. Les pastilles de prix sont ajoutées par le site.
- **Ambiance du site** : lumière naturelle chaude, tons sable, béton, pierre claire et vert sauge, avec une touche d'orange (#FF5A1F) bienvenue, par exemple une veste ou un sac. Éviter le vert citron d'Augment, pour ne pas être confondu avec leur site.
- **Fichiers** : livrer en JPG ou PNG de grande taille ; je les convertis en WebP et je les recadre. Garder de l'espace libre autour du sujet, car le site superpose parfois des pastilles.
- **Personnes** : visages naturels, pas de célébrité ni de personne réelle identifiable.

## Emplacements

| Code | Emplacement | Format | Priorité |
|---|---|---|---|
| H1 | Accueil, haut de page, colonne droite | Portrait 4:5 (1600 × 2000) | 1 |
| L1–L3 | Accueil, nouveau bandeau « Au quotidien » | Paysage 3:2 (1800 × 1200) | 2 |
| S1 | Accueil, section « Le service » | Paysage 3:2 | 3 |
| G1–G4 | Comparatif, cartes des 4 guides | Paysage 4:3 (1600 × 1200) | 3 |
| OG | Image de partage (réseaux sociaux, messageries) | 1200 × 630 | 2 |

## Prompts

**H1 — Hero (les deux modèles ensemble)**
> Editorial lifestyle photograph, portrait 4:5. A sleek black folding electric kick scooter (Augment Agaru, wide handlebar, 10-inch air tyres, battery integrated in the deck) parked next to a compact black foldable electric moped with a seat and small wheels (Augment E-scooter 360), on a sunny pale-stone street in a French city like Bordeaux, golden hour, soft shadows, shallow depth of field, a young adult in a rust-orange jacket holding a helmet, calm premium mood, warm neutral palette, no text, no logos, photorealistic, 50mm lens.

**L1 — Trajet quotidien (Agaru)**
> Photorealistic, landscape 3:2. Commuter riding a black Augment Agaru electric kick scooter on a dedicated bike lane in a French city, morning light, wearing a helmet, motion blur in the background, wet pavement after light rain, warm tones, no text.

**L2 — Rangement en intérieur (E-scooter 360 plié)**
> Photorealistic, landscape 3:2. The black Augment E-scooter 360 folded compactly in a bright apartment entryway next to a wooden bench and coats, natural window light, Scandinavian-meets-Haussmann interior, calm and tidy, no people or a person's hand on the handle, no text.

**L3 — Batterie amovible (E-scooter 360)**
> Photorealistic close-up, landscape 3:2. A person lifting the removable battery out from under the open seat of a black Augment E-scooter 360, carrying it by the handle toward a building door, evening light, focus on hands and battery, no text.

**S1 — Service et entretien**
> Photorealistic, landscape 3:2. A technician in a clean workshop checking the tyre pressure of a black Augment Agaru electric kick scooter, tools neatly arranged, soft daylight, reassuring professional mood, no text, no brand logos on clothing.

**G1 à G4 — Guides** (même lumière que L1–L3)
- G1 : gros plan du plateau de l'Agaru et de son frein à disque arrière, sur fond béton clair.
- G2 : E-scooter 360 garé dans une rue, plaque arrière visible, casque posé sur la selle.
- G3 : smartphone affichant une application de mobilité générique (écran flou), posé sur le guidon de l'Agaru.
- G4 : main qui contrôle la pression d'un pneu de 10 pouces, borne de recharge domestique en arrière-plan.

**OG — Image de partage**
> Clean composition 1200×630, warm off-white background (#EFEDE6), the black Augment Agaru kick scooter and the Augment E-scooter 360 side by side, soft studio floor shadow, generous empty space on the left for a title, no text.

## Inspiration

- Le site augment.eco alterne photos studio sur fond uni et grandes photos de route en plein cadre. On peut reprendre ce rythme sans copier leurs images.
- Les bannières du catalogue AWIN d'Augment se consultent dans votre tableau de bord AWIN, rubrique des outils ou créations publicitaires. L'API ne les fournit pas. Elles sont autorisées pour les affiliés, mais les créations du site restent plus distinctives.

## Une fois les images prêtes

Les déposer dans un dossier, par exemple `D:\AUGMENT ECO\visuels`, puis me prévenir. Je les recadre, je les compresse et je les intègre. Le hero s'active en mode photo (instructions dans `site/index.html`).

---

## Série 2 — « Né dans le sport, pensé pour le quotidien »

Faits tirés de la page « Notre histoire » d'augment.eco :
- skis de Coupe du monde dès 2015 (Pinzgau, Autriche) ;
- or et argent olympiques en saut à ski en 2022 ;
- collaboration avec Red Bull en 2022 ;
- partenaire de l'équipe Red Bull KTM Ajo en MotoGP depuis 2023.

L'idée est de parler à la fois au **professionnel**, qui cherche une alternative pour aller travailler, et au **sportif**.

**À respecter impérativement pour cette série :**
- **Aucun symbole protégé** : ni anneaux olympiques, ni logo ou couleurs Red Bull, KTM, MotoGP ou FIS, ni mot « olympique » écrit dans l'image. Les marques olympiques sont protégées par la loi en France (Code du sport), et les autres sont des marques déposées.
- **Aucun athlète réel reconnaissable** (Manuel Fettner, Marcel Hirscher…) : leur image est protégée par le droit à l'image.
- On évoque l'univers par l'ambiance (montagne, paddock, tenue technique), pas par des logos.
- Mêmes règles produit que la série 1 : véhicules fidèles aux photos de `site/img/`, casque et gants pour le 360, pas de texte.

| Code | Public | Scène | Format |
|---|---|---|---|
| P1 | Pro | Arrivée au bureau en Agaru | Paysage 3:2 (1800 × 1200) |
| P2 | Pro | E-scooter 360 plié dans un hall d'entreprise | Paysage 3:2 |
| P3 | Pro | Pause déjeuner, centre d'affaires | Portrait 4:5 (1600 × 2000) |
| A1 | Sport | Paddock de circuit moto, 360 utilisé comme scooter de paddock | Paysage 3:2 |
| A2 | Sport | Village alpin autrichien, 360 sur route de montagne | Paysage 3:2 |
| A3 | Sport | Sportive allant à l'entraînement en Agaru, à l'aube | Portrait 4:5 |

**P1 — Arrivée au bureau**
> Editorial lifestyle photograph, landscape 3:2. A man in his thirties wearing a navy overcoat, chinos and a helmet, laptop backpack, rides the black Augment Agaru electric kick scooter (match the reference: wide handlebar, 10-inch air tyres, battery in the deck) into the forecourt of a modern glass-and-stone office building in a French business district, early morning light, colleagues walking in the background, calm and efficient mood, warm neutral palette with a touch of orange (#FF5A1F) on a scarf, no text, no logos, photorealistic, 35mm.

**P2 — Rangement au bureau**
> Photorealistic, landscape 3:2. The black Augment E-scooter 360 folded compactly (match the reference folded profile) standing in a bright modern office lobby next to a reception desk and plants, a woman in business attire walking past holding a coffee and her helmet, soft daylight, premium corporate atmosphere, no text, no logos.

**P3 — Pause déjeuner**
> Editorial photograph, portrait 4:5. A woman in smart-casual work clothes, helmet in hand, stands next to the black Augment Agaru parked on a wide sunny sidewalk outside a café in a French business district at lunchtime, relaxed confident smile seen in three-quarter profile, warm natural light, no text, no logos.

**A1 — Paddock**
> Photorealistic, landscape 3:2. A motorsport paddock at a racing circuit, generic team garages with unbranded neutral grey and orange livery, a mechanic in a plain dark team shirt (no logos) rides the black Augment E-scooter 360 between garages wearing a helmet and gloves, racing motorcycles under covers in the background, late afternoon sun, energetic but clean mood, shallow depth of field, absolutely no brand logos, no sponsor names, no text.

**A2 — Montagne**
> Photorealistic, landscape 3:2. A rider wearing a helmet and gloves rides the black Augment E-scooter 360 on a small paved road through an Austrian alpine village in summer (wooden chalets with flower boxes, green meadows, high peaks with a little snow), crisp morning light, sense of freedom and performance, no text, no logos.

**A3 — Entraînement**
> Editorial photograph, portrait 4:5. A young female athlete in technical running gear with a sports bag, wearing a helmet, rides the black Augment Agaru electric kick scooter along a riverside bike path toward a stadium at dawn, mist on the water, golden backlight, determined calm expression in profile, no text, no logos, photorealistic.

**Intégration prévue** : une section de l'accueil « Né dans le sport de haut niveau », avec les faits ci-dessus (Coupe du monde de ski, médailles 2022, MotoGP depuis 2023), deux ou trois de ces photos, et un double message, pro d'un côté, sport de l'autre.

---

## H2 — Nouvelle image du haut de l'accueil (plein cadre)

Le haut de l'accueil n'utilise plus de carré : la photo occupe toute la droite de l'écran et se fond dans le fond de page sur son bord gauche. Le texte est à gauche, sans pastilles.

- **Format** : très large, 2400 × 1200 px (2:1), JPG ou PNG. Remplacer `site/img/hero.webp` (je convertis et je règle le cadrage).
- **Composition** : sujet principal sur le **tiers droit et le centre**. Le **tiers gauche doit rester calme** (mur, ciel, flou, ton sable), sans élément important : c'est là que passent le titre et le texte.
- **Qualité** : image nette, sans déformation. Les deux véhicules doivent être fidèles aux photos de référence (`site/img/`). Pas de texte ni de logo, pas de plaque lisible, pas de visage reconnaissable.
- **Fond de raccord** : les tons du côté gauche doivent se rapprocher de #EFEDE6 (beige clair), pour que le fondu soit invisible.

> Wide editorial lifestyle photograph, 2:1 landscape, 2400×1200. On the right two-thirds: the black Augment Agaru electric kick scooter (match the reference: wide handlebar, 10-inch air tyres, battery integrated in the deck) and the black Augment E-scooter 360 compact folding electric moped (match the reference), parked side by side on a sunny pale-stone street in Bordeaux, golden hour, soft long shadows, a person in a rust-orange jacket walking away in the background holding a helmet. The left third of the frame is calm and uncluttered: soft out-of-focus limestone facade and warm light fading to a light beige (#EFEDE6), no important detail there. Shallow depth of field, premium calm mood, photorealistic, 35mm, no text, no logos, no readable licence plate.

Variante « professionnels » à tester : même composition, mais en fin de matinée devant un immeuble de bureaux vitré, la personne en tenue de ville avec un sac pour ordinateur.
