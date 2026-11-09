# Tâches avant mise en ligne — 08/11/2026

Objectif : site déployable ce soir sur Vercel.

| # | Tâche | Détail | État |
|---|---|---|---|
| 1 | Accroche du haut de page | « Déplacez-vous en toute liberté. » + philosophie de la marque, sans détails techniques | Fait |
| 2 | Vitesse (Lighthouse) | Images redimensionnées par taille d'écran (srcset), compression, chargement différé, polices, préconnexion vers AWIN et augment.eco, cache Vercel | Fait |
| 3 | SEO technique | Titres et descriptions par page, balises Open Graph, données structurées (Organization, Product, FAQ, Breadcrumb), sitemap.xml, robots.txt, URL canoniques, textes alternatifs | Fait (relancer tools/set_domain.py avec le vrai domaine et le nom avant déploiement) |
| 4 | Tracker de prix | `python site/tools/tracker_prix.py [--appliquer]` : relève prix, acomptes, financement, stock et délais sur augment.eco (France), signale les écarts, corrige les montants sans ambiguïté (pages, articles, générateurs) | Fait ; reste : lancement automatique quotidien (à valider) et source des promotions |
| 5 | Nom du site | Remplacer « Guide Augment Eco » (pas présenté comme un guide) : propositions puis choix | Fait : Roulelibre |
| 6 | Nom de domaine | Recherche sur IONOS d'un .fr ou .com disponible et peu cher, pour le nom choisi | roulelibre.fr choisi : à acheter sur IONOS |
| 7 | Articles de base | 4 articles en ligne dans `site/conseils/` (location ou achat, assurance et règles, écologie, scooter 45 km/h) ; suite du cocon dans `COCON.md` | Fait |
| 8 | Déploiement | Mise en ligne sur Vercel, domaine branché, vérification finale (liens AWIN, mentions légales, cookies) | À faire |

| 9 | Logo et favicon | Piste D (oiseau-roue) retenue ; autres pistes conservées dans `visuels/logo/propositions` ; script `site/tools/logo_final.py` | Fait |

Plus tard : multilingue, autres images (lot 2), mentions légales à compléter (SIREN, e-mail, directeur de publication).
