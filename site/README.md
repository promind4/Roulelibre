# Roulelibre — site statique

Site éditorial (HTML, CSS et JavaScript simples, sans framework ni étape de build).

## Lancer en local

```
python -m http.server 8090 --directory site
```

Puis ouvrir http://localhost:8090/index.html

## Structure

| Fichier | Rôle |
|---|---|
| `index.html` + `css/home.css` | Accueil : hero, chiffres clés, gamme, service, parcours d'abonnement |
| `configurateur.html` + `css/configurateur.css` + `js/configurateur.js` | Fiche produit et simulateur (abonnement, achat, financement). Toutes les données et tous les prix sont dans `js/configurateur.js` |
| `comparateur.html` + `css/comparateur.css` + `js/comparateur.js` | Comparatif des 14 critères, entreprises, avis, guides, FAQ |
| `mentions-legales.html`, `confidentialite.html` + `css/legal.css` | Pages légales. Les informations à compléter sont surlignées (`<span class="todo">`) |
| `videos.html` + `js/videos.js` | Page des vidéos YouTube et lecteur intégré. La liste des vidéos (une ligne par vidéo) est dans `js/videos.js`, partagée avec le bandeau de l'accueil |
| `css/style.css` | Système commun : couleurs, typographies, boutons, cartes, en-tête, pied de page, cookies |
| `js/main.js` | Comportements communs : menu mobile, en-tête, apparitions, bandeau cookies |
| `tools/partials/` | Modèles de l'en-tête, du pied de page et du `<head>`, à recopier dans chaque page en cas de modification |
| `img/` | Visuels produits (WebP détourés) |

## Bandeau d'offres et adresses

- Le bandeau noir en haut de chaque page (`data-promo`) sert aux offres et nouveautés Augment. Sans promotion, il met en avant un prix relevé : à mettre à jour sur toutes les pages en même temps que les prix. Source prévue : promotions AWIN d'Augment (API `POST /publisher/3099440/promotions`) et veille des prix d'augment.eco.
- `vercel.json` active les adresses sans extension sur Vercel : `/videos`, `/comparateur`, etc. Les liens internes en `.html` y sont redirigés automatiquement.

## Remplacer les images

Chaque emplacement est précédé d'un commentaire `<!-- IMAGE À REMPLACER : ... -->` qui indique le cadrage attendu. Le brief des visuels à générer, avec les prompts, est dans `../BRIEF_VISUELS.md`.
Les emplacements ont un ratio fixe et affichent l'image entière, centrée et posée en bas (`object-fit: contain`).
Pour une photo d'ambiance plein cadre, remplacer `contain` par `cover` sur l'emplacement concerné.
Penser à mettre à jour les attributs `width` et `height` de la balise `<img>`.

## Mettre à jour les prix

La source de vérité est augment.eco : relever les chiffres dans le configurateur de chaque fiche produit (onglets Achat et Abonnement, fenêtre « Options de financement »), pas dans la description de la page.
Les grilles d'abonnement complètes (3 durées × 5 acomptes, avec l'économie totale) sont dans `js/configurateur.js` (`sub`).

Les prix figurent dans les trois pages HTML et dans `js/configurateur.js`, avec la date de relevé (07/11/2026).
À chaque changement, mettre à jour la date dans toutes les mentions « Prix relevés le … ».

## Liens vers augment.eco (AWIN)

Tous les liens partenaires passent par AWIN (programme 131358, France uniquement, liens profonds autorisés).

- Boutons par modèle (accueil, comparatif) : lien profond vers la fiche produit, `https://www.awin1.com/cread.php?awinmid=131358&awinaffid=3099440&ued=<adresse encodée>&platform=pl`.
- Bouton du simulateur : lien profond vers le tunnel de commande, pré-rempli (`checkoutUrl` dans `js/configurateur.js`) :
  `https://augment.eco/fr-fr/checkout/configure?scooterName=…&mode=subscription|purchase&addonIds=…&serviceIds=…&accessoryIds=…`
  - `scooterName` : `agaru-smart`, `agaru-ultra`, `augment-360`.
  - `serviceIds` : `E-Scooter-All-Inclusive-Maintenance` (Ultra en abonnement), `Theft-coverage` (couverture vol).
  - `accessoryIds` : clignotants `Agaru-Turning-Signals-RECURRING-0` (abonnement) ou `Agaru-Turning-Signals-Charge-ONE_TIME-0` (achat) ; 2e batterie du 360 `360-1080-Wh-Battery-Extra-Charge-ONE_TIME-69000`.
  - La durée, l'acompte et la taille du casque ne passent pas par l'adresse : l'utilisateur les choisit chez Augment (indiqué sous le bouton).
  - Ces identifiants sont internes à Augment et peuvent changer : à contrôler lors de chaque relevé de prix.
- La clé de l'API AWIN est rangée hors du site, dans `_prive/`. Ne jamais la placer dans `site/`.

## Cache des navigateurs

Les feuilles de style et les scripts sont appelés avec un numéro de version (`css/style.css?v=20261107c`).
À chaque modification d'un fichier CSS ou JS, changer ce numéro dans toutes les pages et dans `tools/partials/`. Sinon, les navigateurs gardent l'ancienne version et la page peut s'afficher cassée.

## Outils de vérification

- `python tools/shoot.py <url> <dossier> 1440 390` : captures pleine page, signale les débordements et les erreurs JavaScript.
- `python tools/overflow.py <url> 320 1440 20` : recherche de débordement horizontal sur une plage de largeurs.

Ces deux outils nécessitent Python avec Playwright et Google Chrome.

## Reste à faire avant la mise en ligne

- Compléter les champs surlignés des pages légales : éditeur, hébergeur, e-mail de contact, outil d'audience, durées (`grep -n 'class="todo"' *.html`).
- Rédiger les 4 guides (affichés « À paraître »).
- Brancher réellement la mesure d'audience et le suivi AWIN sur le consentement enregistré (`localStorage` : `ae-consent-v1`, valable 6 mois, événement `consent:change`).
- Mettre en place une veille automatique d'augment.eco (prix, paliers d'acompte, financement) pour signaler tout changement.
