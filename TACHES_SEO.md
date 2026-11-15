# Liste de tâches — 15/11/2026

Légende : ✅ fait et vérifié · 🔶 fait, action de l'utilisateur à finir · ⏳ à planifier · ❌ non fait

## 1. Illustrations animées des articles
| # | Tâche | État | Vérification |
|---|---|---|---|
| 1.1 | 10 illustrations SVG animées (une par article restant), générateur `site/tools/illustrations_conseils.py` | ✅ | planche contact relue, `verifier_liens.py` : tout est bon |
| 1.2 | Image de partage (JPG 1200×630) pour chaque illustration, `site/tools/rendre_og.py` | ✅ | 10 fichiers `anim-*-og.jpg` |
| 1.3 | Articles, vignettes de la rubrique et de l'accueil branchés sur les SVG, sitemap images régénéré | ✅ | 17 URL au sitemap |
| 1.4 | Animations coupées si « réduire les animations » demandé | ✅ | règle `prefers-reduced-motion` dans chaque SVG |
| 1.5 | Relire le mouvement de chaque scène dans un vrai navigateur (couleurs, rythme) | 🔶 | à faire par l'utilisateur : ouvrir chaque article |

## 2. Mots-clés (Search Console)
| # | Tâche | État | Vérification |
|---|---|---|---|
| 2.1 | Relever les requêtes réelles (90 jours) | ✅ | `site/tools/data/gsc_requetes.json` : 50 requêtes, 23 pages |
| 2.2 | Valider ou écarter chaque requête et la rattacher à une page | ✅ | tableau dans `MOTS_CLES.md` |
| 2.3 | Appliquer ce qui est justifié (H2 assurance avec « amende sans assurance ») | ✅ | article reconstruit |
| 2.4 | Refaire le relevé dans 4 semaines | ⏳ | `python _gsc_requetes.py` |

## 3. Balises et Umami
| # | Tâche | État | Vérification |
|---|---|---|---|
| 3.1 | Balise Umami générée sur toutes les pages à partir de `site/tools/data/umami.json` | ✅ | testée avec un faux identifiant, puis retirée |
| 3.2 | Événement « clic-partenaire » (AWIN et augment.eco) avec page, produit, texte du lien | ✅ | `site/js/main.js`, sans effet tant qu'Umami n'est pas chargé |
| 3.3 | Phrase « mesure d'audience sans cookie » ajoutée automatiquement à la page confidentialité à l'activation | ✅ | marqueur testé |
| 3.4 | Site « Roulelibre » créé dans Umami, identifiant branché sur les 19 pages | ✅ | balise vérifiée en ligne |
| 3.4b | Suivi détaillé anonyme : clics partenaires, simulateur, galerie, FAQ, vidéos, défilement, temps de lecture, fin d'article | ✅ | testé en local avec un faux Umami, en ligne depuis le push |
| 3.5 | Vérifier qu'une visite apparaît dans Umami et qu'un clic partenaire crée un événement | ⏳ | après 3.4 |

## 4. Audit SEO organique
| # | Constat | Priorité | État |
|---|---|---|---|
| 4.1 | 16 pages sur 17 indexées par Google (inspection d'URL) | — | ✅ |
| 4.2 | **/configurateur** : « Google ne reconnaît pas cette URL » (jamais explorée), alors qu'aucun blocage technique n'existe (200, canonical, pas de noindex, au sitemap et au menu) | Haute | 🔶 Search Console > Inspection d'URL > Demander l'indexation |
| 4.3 | Rapport sitemap : « 0 indexée » malgré l'inspection positive, simple retard du rapport | Basse | ⏳ revérifier dans 1 semaine |
| 4.4 | Vitesse mobile mesurée en direct : LCP 0,5 à 0,9 s, CLS 0, 270 à 610 Ko par page | — | ✅ |
| 4.5 | Titres 29 à 61 caractères, descriptions 101 à 159, un seul H1 par page, aucune image sans alt ni dimensions, aucun doublon | — | ✅ |
| 4.6 | Données structurées : Organization, WebSite, Article, FAQPage, Product, ItemList, BreadcrumbList sur les bonnes pages | — | ✅ |
| 4.7 | Anciennes adresses `.html` et `roulelibre.fr` (sans www) encore vues par Google : redirections 308 en place, elles disparaîtront d'elles-mêmes | Basse | ⏳ |
| 4.8 | Aucun lien entrant externe : principal frein pour « location / abonnement trottinette électrique » (positions 70 à 90) | Haute | ❌ à lancer : annuaires, YouTubeurs, forums, presse locale |
| 4.9 | Pas d'expérience d'usage réelle ni de photos personnelles (E-E-A-T) | Moyenne | 🔶 à fournir |
| 4.10 | Réseaux sociaux / YouTube pour `sameAs` | Basse | 🔶 à fournir |
| 4.11 | Pages locales (Bordeaux, Paris…) : seulement avec une vraie valeur locale | Basse | ⏳ décision de l'utilisateur |
| 4.12 | Articles « Agaru Ultra avis », « Augment 360 avis » (seulement avec expérience réelle) | Moyenne | ⏳ |
| 4.13 | roulelibree.vercel.app redirigé (308) vers www, noindex sur les autres adresses vercel.app | Basse | ✅ en local, à vérifier après push |
| 4.14 | Section « Autonomie et temps de charge » (article batterie) + FAQ, H2 « Quel permis pour un scooter 45 km/h ? » | Moyenne | ✅ |
| 4.15 | Liens internes depuis le contenu : accueil 2 → 13, vidéos 1 → 13, comparatif 10 → 14 | Moyenne | ✅ |
| 4.16 | Relevé des prix augment.eco du 15/11 : aucun écart | Moyenne | ✅ |
| 4.17 | Pages produits Agaru Ultra, E-scooter 360, Agaru Smart | Haute | ⏳ prochaine étape |
