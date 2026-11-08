# Cocon sémantique Roulelibre — 08/11/2026

Principe : chaque article de niche répond à une question précise, renvoie vers son article « mère » (plus large), qui renvoie vers une page qui convertit (simulateur, comparatif, fiche Augment en lien partenaire). Les articles d'un même cocon se citent entre eux ; on évite les liens entre cocons, sauf quand le lecteur en a vraiment besoin.

```
Accueil / Comparatif / Simulateur   ← pages qui convertissent
        ↑
Articles mères (4 en ligne)
        ↑
Articles de niche (à écrire)        ← portes d'entrée longue traîne
```

Rubrique : entrée 05 « Guides & conseils » du menu (`site/conseils/index.html`) ; le comparatif renvoie vers les articles publiés dans sa section « Guides & conseils ».

Contenu : `site/tools/articles_contenu.py` (un dict par article), puis `python tools/build_articles.py` et `python tools/set_domain.py` (sitemap). Images dans `site/img/conseils/` (version 1536 px + `-800`).

## 1. Budget et location (cocon prioritaire, le plus proche de l'achat)

Mère en ligne : **Louer ou acheter une trottinette électrique** (`louer-ou-acheter-trottinette-electrique`). Destination : simulateur.

| Article de niche à écrire | Requête visée | Angle |
|---|---|---|
| **En ligne (08/11)** : Forfait mobilités durables (`forfait-mobilites-durables-trottinette-electrique`) | forfait mobilité durable trottinette électrique | 600 €/an, 900 € en cumul ; trottinette personnelle ou louée éligible ; scooter éligible loué, pas acheté (FAQ ministère, 27/03/2026) |
| Trottinette électrique en paiement en plusieurs fois : LOA, leasing, crédit, quelles différences ? | trottinette électrique paiement en plusieurs fois, LOA, leasing | tableau des 3 formules, ce qui est compris ou non, coût total |
| Location longue durée de trottinette : ce qui est compris (et ce qui ne l'est pas) | location trottinette électrique longue durée | réparations, pièces d'usure, vol, fin de contrat, option d'achat |
| Combien coûte une trottinette électrique par mois, tout compris ? | coût trottinette électrique par mois | recharge (quelques euros par an), assurance, entretien, comparaison avec pass transport et voiture |
| Trottinette électrique pour étudiant : budget et astuces | trottinette électrique étudiant | location sans gros acompte, campus, stationnement |

## 2. Règles, assurance, sécurité

Mère en ligne : **Assurance et réglementation** (`trottinette-electrique-assurance-reglementation`). Destination : comparatif, puis couverture vol.

| Article de niche à écrire | Requête visée | Angle |
|---|---|---|
| Trottinette électrique volée : que faire ? | trottinette électrique volée que faire | dépôt de plainte, numéro de série, couverture vol (franchise 100 / 150 €), antivol |
| Rouler sous la pluie en trottinette électrique | trottinette électrique pluie | indice d'étanchéité, freinage, entretien après la pluie |
| Trottinette électrique la nuit : éclairage et gilet | trottinette électrique la nuit éclairage obligatoire | ce que dit le Code de la route, équipement |
| Prendre le train ou le bus avec sa trottinette électrique | trottinette électrique dans le train TER TGV | règles SNCF, pliage, poids (20 kg) |
| Quel casque pour une trottinette électrique ? | casque trottinette électrique | recommandé vs obligatoire, casque vélo ou casque moto (pour le 360) |

## 3. Écologie et ville

Mère en ligne : **La trottinette électrique est-elle écologique ?** (`trottinette-electrique-ecologique`). Destination : location (réparations comprises = durée de vie plus longue).

| Article de niche à écrire | Requête visée | Angle |
|---|---|---|
| Batterie de trottinette électrique : durée de vie et recyclage | batterie trottinette électrique durée de vie, recyclage | cycles de charge, bonnes pratiques, filière de collecte |
| Remplacer sa voiture par une trottinette électrique : le test sur un mois | remplacer voiture par trottinette | à écrire **seulement avec une vraie expérience** (règle E-E-A-T) |
| Trajet domicile-travail en trottinette : jusqu'à quelle distance ? | trottinette électrique trajet domicile travail | autonomie réelle, temps de trajet, combinaison train + trottinette |
| Trottinette électrique et zones à faibles émissions (ZFE) | ZFE trottinette électrique | ce qui change pour les voitures, l'alternative 25 km/h et 45 km/h |

## 4. Scooter électrique 45 km/h

Mère en ligne : **Scooter électrique pliable 45 km/h** (`scooter-electrique-pliable-45-km-h`). Destination : fiche 360 et simulateur (location dès 25,90 €/mois).

| Article de niche à écrire | Requête visée | Angle |
|---|---|---|
| Trottinette ou scooter électrique : lequel choisir ? | trottinette électrique ou scooter | distances, vitesse, permis, budget ; pont entre les cocons 2 et 4 |
| Permis AM (ex-BSR) : qui en a besoin et comment l'obtenir ? | permis AM scooter électrique | né avant 1988, formation, coût |
| Ranger un scooter électrique en appartement | scooter électrique pliable appartement | dimensions pliées, ascenseur, recharge de la batterie amovible |
| Assurance scooter électrique 50 cc : combien ça coûte ? | assurance scooter électrique prix | fourchettes indicatives et sources, sans recommander d'assureur |

## 5. Choisir sa trottinette (à ouvrir ensuite)

Mère à écrire : **Comment choisir sa trottinette électrique ?** (autonomie, poids, freins, roues, pliage). Destination : comparatif.

Niches : trottinette électrique adulte lourde (charge maximale), autonomie réelle vs annoncée, trottinette électrique pliable légère, Agaru Smart ou Agaru Ultra (reprend le guide 01 du comparatif), entretien et pression des pneus (guide 04).

## Guides annoncés dans l'ancien comparatif (texte à rédiger)

Les cartes « À paraître » du comparatif ont été retirées (images archivées dans `visuels/site-non-utilisees/guides-comparatif/`). Leurs sujets deviennent des articles de la rubrique :

- Agaru Smart ou Agaru Ultra : les 768 Wh valent-ils l'écart de prix ? (cocon 5)
- Service « Tout est couvert » et couverture vol à 2,95 €/mois : comment ça marche ? (cocon 1 ou 2, avec « trottinette volée »)
- Entretien, pression des pneus et charge de la batterie (cocon 5)

## Images des articles

**Nouvelle direction (08/11, à valider sur le premier test)** : illustration animée en SVG + CSS, aux couleurs du site (orange #FF5A1F, crème, encre) avec des tons chauds et gais (soleil, pêche, moutarde, vert sapin). Exemple : `site/tools/illustration_fmd.py` → `site/img/conseils/anim-fmd.svg` (+ `anim-fmd-og.jpg` pour le partage, rendu avec Chrome sans interface). Dans `articles_contenu.py`, ajouter `anim=True`. Les photos actuelles des 4 premiers articles sont jugées grises et tristes : à remplacer.

Ancienne approche : photos naturelles liées au sujet, pas de mise en avant du produit (table avec carnet de calculs, piste cyclable sous la pluie, casque dans l'entrée…). Prompts : scratchpad `make_prompts7.py` (style documentaire, aucun texte lisible, aucune marque). Fichiers sources dans `visuels/generes/articles/`, anciennes images dans `visuels/site-non-utilisees/conseils-v1/`.

## Ordre conseillé

1. Forfait mobilités durables (fort volume, lecteur proche de la décision)
2. Trottinette volée : que faire ? (couverture vol, conversion location)
3. Trottinette ou scooter électrique ?
4. Comment choisir sa trottinette électrique (nouvelle mère)
5. Paiement en plusieurs fois / LOA / leasing
6. Le reste selon les données Search Console (requêtes avec impressions mais peu de clics = articles à écrire ou à enrichir)

## Règles de rédaction (rappel)

- Ton simple et amical, peu de technique hors comparatif ; une idée par paragraphe, encadré « En bref » en tête.
- Chiffres sourcés (lien en bas d'article), prix relevés sur augment.eco France uniquement (tracker).
- Jamais d'essai inventé. Les articles « test / avis » attendent une vraie expérience.
- Relecture anti-schémas IA sans retirer les mots-clés.
- Images : personnes stylées, multiculturelles, style documentaire ; homme ou véhicule seul sur les visuels de présentation.
- Pas de marque « Augment » dans la publicité payante (conditions AWIN) ; le contenu éditorial est autorisé.
