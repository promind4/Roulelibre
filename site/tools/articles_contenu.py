# -*- coding: utf-8 -*-
"""Contenu des articles de la rubrique Conseils (cocon sémantique, voir D:\\AUGMENT ECO\\COCON.md).
Chaque article : métadonnées, « en bref », corps HTML, FAQ, sources, articles liés.
Règles de rédaction : ton amical, phrases courtes, pas de tiret long, chiffres sourcés, jamais d'essai inventé."""

AWIN = 'https://www.awin1.com/cread.php?awinmid=131358&amp;awinaffid=3099440&amp;ued={}&amp;platform=pl'
ULTRA = AWIN.format('https%3A%2F%2Faugment.eco%2Ffr-fr%2Fagaru-ultra%2F')
SMART = AWIN.format('https%3A%2F%2Faugment.eco%2Ffr-fr%2Fagaru-smart%2F')
S360 = AWIN.format('https%3A%2F%2Faugment.eco%2Ffr-fr%2Faugment-360%2F')

def lien_partenaire(url, texte):
    return '<a class="btn btn--ink" href="%s" target="_blank" rel="sponsored noopener" title="Lien partenaire">%s <span class="arr" aria-hidden="true">→</span></a>' % (url, texte)

ARTICLES = [
# ---------------------------------------------------------------------------------------------
dict(
 slug='forfait-mobilites-durables-trottinette-electrique',
 categorie='Budget',
 titre_seo='Forfait mobilités durables trottinette : jusqu’à 600 €/an',
 description='Votre employeur peut prendre en charge jusqu’à 600 € par an de vos trajets en trottinette électrique, personnelle ou louée. Qui y a droit, comment le demander.',
 h1='Forfait mobilités durables&nbsp;: et si votre employeur payait votre trottinette&nbsp;?',
 chapo='Jusqu’à 600&nbsp;€ par an, sans impôt ni cotisations, pour venir au travail en trottinette électrique. Le forfait mobilités durables existe depuis 2020, et pourtant beaucoup de salariés ne pensent même pas à le demander. Voici comment ça marche, simplement.',
 image=('anim-fmd', 'Illustration animée : un salarié file en trottinette électrique dans une ville ensoleillée, une fiche de paie validée et des pièces en euros s’envolent derrière lui'),
 anim=True,
 lecture=5,
 en_bref=[
  'Le forfait mobilités durables permet à votre employeur de financer vos trajets domicile-travail en trottinette électrique, à vélo ou en covoiturage.',
  'Jusqu’à 600&nbsp;€ par an sans impôt ni cotisations, et jusqu’à 900&nbsp;€ s’il s’ajoute au remboursement d’un abonnement de transport.',
  'Trottinette personnelle ou louée&nbsp;: les deux comptent. Un scooter 45&nbsp;km/h compte s’il est loué, pas s’il vous appartient.',
  'Dans le privé, il n’a rien d’automatique&nbsp;: c’est à demander.',
 ],
 corps='''
<h2 id="c-est-quoi">Le forfait mobilités durables, c’est quoi&nbsp;?</h2>
<p>C’est une somme que votre employeur vous verse pour encourager les trajets domicile-travail moins polluants. On l’appelle souvent FMD. Elle apparaît sur la fiche de paie, ou arrive sur une carte prépayée appelée titre-mobilité, sur le modèle des titres-restaurant.</p>
<p>Son gros atout&nbsp;: jusqu’au plafond, elle n’est soumise ni à l’impôt sur le revenu ni aux cotisations sociales. Ce que vous recevez, vous le gardez en entier. Et pour l’entreprise, c’est moins cher qu’une augmentation de salaire du même montant.</p>

<h2 id="eligible">Trottinette, location, scooter&nbsp;: qu’est-ce qui compte&nbsp;?</h2>
<p>Le ministère de la Transition écologique liste les modes de transport acceptés. Bonne nouvelle&nbsp;: la trottinette électrique y figure, que vous l’ayez achetée ou louée.</p>
<ul class="check">
 <li>votre <strong>trottinette électrique personnelle</strong>&nbsp;;</li>
 <li>la <strong>location</strong> d’une trottinette, d’un cyclomoteur ou d’une moto, <strong>quelle que soit la durée</strong>&nbsp;: une Agaru Ultra ou un E-scooter 360 en abonnement entrent donc dans le cadre&nbsp;;</li>
 <li>le vélo, électrique ou non, le covoiturage, l’autopartage de véhicules électriques et les transports en commun hors abonnement.</li>
</ul>
<p>Ce qui ne compte pas&nbsp;:</p>
<ul class="dash">
 <li>un scooter électrique qui vous appartient&nbsp;;</li>
 <li>la marche, la trottinette mécanique, le skateboard, le taxi et les VTC.</li>
</ul>
<aside class="tip"><p class="tip__t">Bon à savoir</p><p>Pour un scooter 45&nbsp;km/h comme l’E-scooter 360, la formule change tout&nbsp;: acheté, il n’ouvre pas droit au forfait&nbsp;; loué, si. De quoi peser dans la balance si vous hésitez entre les deux.</p></aside>

<h2 id="combien">Combien peut-on toucher&nbsp;?</h2>
<p>Dans le privé, le plafond sans impôt ni cotisations est de <strong>600&nbsp;€ par an</strong>. Si votre employeur rembourse aussi une partie de votre abonnement de transport, l’ensemble peut monter jusqu’à <strong>900&nbsp;€</strong>. C’est l’entreprise qui fixe le montant, par accord collectif ou par décision de l’employeur, avec les mêmes règles pour tous les salariés.</p>
<p>Dans la fonction publique, le forfait dépend du nombre de jours où vous venez en mode doux&nbsp;: 100&nbsp;€ par an à partir de 30&nbsp;jours, 200&nbsp;€ à partir de 60, 300&nbsp;€ à partir de 100.</p>
<p>Concrètement, que représentent 600&nbsp;€ face au prix d’une location&nbsp;? Voici l’exemple d’un employeur qui verse le maximum.</p>
<div class="art-table-wrap">
<table class="art-table">
 <caption>Exemple avec un forfait de 600&nbsp;€ par an (tarifs augment.eco France, hors options)</caption>
 <thead><tr><th scope="col">Formule</th><th scope="col">Coût sur un an</th><th scope="col">Reste à payer</th></tr></thead>
 <tbody>
  <tr><th scope="row">Agaru Ultra, 12&nbsp;mois, acompte 399&nbsp;€</th><td>554,40&nbsp;€</td><td><strong>0&nbsp;€</strong></td></tr>
  <tr><th scope="row">Agaru Ultra, 36&nbsp;mois, acompte 59&nbsp;€ (1<sup>re</sup> année)</th><td>418,40&nbsp;€</td><td><strong>0&nbsp;€</strong></td></tr>
  <tr><th scope="row">Agaru Ultra, 36&nbsp;mois (années suivantes)</th><td>359,40&nbsp;€</td><td><strong>0&nbsp;€</strong></td></tr>
  <tr><th scope="row">E-scooter 360, 36&nbsp;mois, acompte 290&nbsp;€ (1<sup>re</sup> année)</th><td>1&nbsp;068,80&nbsp;€</td><td>468,80&nbsp;€</td></tr>
  <tr><th scope="row">E-scooter 360, 36&nbsp;mois (années suivantes)</th><td>778,80&nbsp;€</td><td>178,80&nbsp;€</td></tr>
 </tbody>
</table>
</div>
<p>Avec un forfait complet, la location d’une Agaru Ultra ne vous coûte plus rien. Pour le 360, il reste environ 15&nbsp;€ par mois à votre charge après la première année. Et si votre entreprise verse moins, disons 300&nbsp;€, cela couvre déjà une bonne partie de l’abonnement.</p>

<h2 id="demander">Comment le demander à votre employeur</h2>
<ol>
 <li><strong>Vérifiez s’il existe déjà.</strong> Regardez l’intranet, l’accord d’entreprise ou posez simplement la question au service RH. Il est parfois en place sans que personne n’en parle.</li>
 <li><strong>S’il n’existe pas, proposez-le.</strong> Les arguments ne manquent pas&nbsp;: pas de cotisations jusqu’à 600&nbsp;€, moins de places de parking à prévoir, des salariés qui arrivent à l’heure et de bonne humeur.</li>
 <li><strong>Fournissez le justificatif demandé.</strong> Le plus souvent une attestation sur l’honneur, parfois votre facture de location. Une mensualité fixe rend l’exercice très simple.</li>
 <li><strong>Recevez le forfait</strong> sur votre fiche de paie ou sur votre carte titre-mobilité.</li>
</ol>

<h2 id="location">Pourquoi la location va bien avec le forfait</h2>
<p>Une trottinette achetée compte aussi, bien sûr. Mais la location a quelques atouts pratiques&nbsp;: une facture mensuelle facile à présenter, un montant connu à l’avance qui se compare directement au forfait, et pour l’Agaru Ultra, les réparations comprises. Votre trajet ne s’arrête pas au premier pneu crevé. Pour peser le pour et le contre, notre article <a href="louer-ou-acheter-trottinette-electrique.html">louer ou acheter sa trottinette électrique</a> fait le calcul sur 12, 24 et 36&nbsp;mois.</p>
''',
 cta=dict(titre='Combien coûterait votre location, forfait déduit&nbsp;?', texte='Le simulateur reprend la grille réelle d’Augment&nbsp;: choisissez la durée et l’acompte, puis comparez la mensualité avec le forfait proposé par votre employeur.',
          boutons=['<a class="btn btn--primary" href="../configurateur.html?model=ultra">Simuler ma location <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(ULTRA, 'Voir l’Agaru Ultra sur augment.eco')]),
 faq=[
  ('La trottinette électrique est-elle éligible au forfait mobilités durables ?', 'Oui. La trottinette électrique personnelle fait partie des modes acceptés, tout comme la location d’une trottinette, quelle que soit la durée.'),
  ('Quel est le montant du forfait mobilités durables ?', 'Dans le privé, jusqu’à 600 € par an sans impôt ni cotisations, et jusqu’à 900 € en cumul avec la prise en charge d’un abonnement de transport. Dans la fonction publique, de 100 € à 300 € par an selon le nombre de jours de trajet en mode doux.'),
  ('Le forfait mobilités durables est-il obligatoire ?', 'Non, dans le secteur privé il est facultatif : l’employeur décide de le proposer et en fixe le montant, avec les mêmes règles pour tous les salariés.'),
  ('Un scooter électrique est-il éligible au forfait mobilités durables ?', 'Oui s’il est loué, puisque la location de cyclomoteurs fait partie des modes acceptés. Non s’il vous appartient : les scooters personnels ne sont pas éligibles à ce jour.'),
 ],
 sources=[('FAQ forfait mobilités durables, ministère de la Transition écologique (mise à jour du 27 mars 2026)', 'https://www.ecologie.gouv.fr/politiques-publiques/faq-forfait-mobilites-durables-fmd'),
          ('Forfait mobilités durables : conditions d’exonération, Urssaf', 'https://www.urssaf.fr/portail/home/employeur/calculer-les-cotisations/les-elements-a-prendre-en-compte/les-frais-professionnels/les-frais-de-transport/trajet-domicilelieu-de-travail/prise-en-charge-facultative-des/forfait-mobilites-durables.html'),
          ('Tarifs de location : tunnel de commande augment.eco (France)', 'https://augment.eco/fr-fr/agaru-ultra/')],
 lies=['louer-ou-acheter-trottinette-electrique', 'prendre-le-train-avec-sa-trottinette-electrique', 'scooter-electrique-pliable-45-km-h'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='louer-ou-acheter-trottinette-electrique',
 categorie='Location',
 titre_seo='Louer ou acheter une trottinette électrique : que choisir ?',
 description='Location longue durée, achat comptant ou paiement en plusieurs fois : le vrai coût d’une trottinette électrique sur 12, 24 et 36 mois, chiffres à l’appui.',
 h1='Louer ou acheter sa trottinette électrique&nbsp;: le match, chiffres à l’appui.',
 chapo='Payer 549&nbsp;€ d’un coup, ou quelques dizaines d’euros par mois avec les réparations comprises&nbsp;? La réponse dépend surtout de combien de temps vous comptez la garder. On a fait les calculs avec les vrais tarifs d’Augment.',
 image=('art-location-budget', 'Sur une table de cuisine, un carnet de calculs, un téléphone en mode calculatrice, un café et un casque : le moment de comparer location et achat d’une trottinette électrique'),
 lecture=6,
 en_bref=[
  'Sur 12 mois avec l’acompte maximal, louer une Agaru Ultra coûte 554,40&nbsp;€, presque le prix d’achat (549&nbsp;€), réparations comprises en plus.',
  'Sur 36 mois, la location revient plus cher que l’achat comptant (de 1&nbsp;009&nbsp;€ à 1&nbsp;137&nbsp;€ selon l’acompte).',
  'Ce que vous payez en plus, c’est la tranquillité&nbsp;: pannes, pneus, freins et batterie sont couverts, avec une trottinette de remplacement.',
  'Vous voulez la garder 4 ou 5 ans et bricoler vous-même&nbsp;? L’achat est plus logique.',
 ],
 corps='''
<h2 id="trois-facons">Trois façons de rouler en Augment</h2>
<p>Chez Augment, il existe trois manières d’avoir sa trottinette&nbsp;:</p>
<ul>
 <li><strong>L’achat comptant</strong>&nbsp;: 399&nbsp;€ pour l’Agaru Smart, 549&nbsp;€ pour l’Agaru Ultra. Elle est à vous, point.</li>
 <li><strong>Le paiement en plusieurs fois</strong>&nbsp;: un crédit PayPal sur 24&nbsp;mois (19,33&nbsp;€/mois pour la Smart, 26,59&nbsp;€/mois pour l’Ultra, TAEG fixe 15,99&nbsp;%). Pratique, mais c’est un crédit&nbsp;: il vous engage et doit être remboursé.</li>
 <li><strong>La location longue durée</strong> (Augment parle d’abonnement ou de leasing)&nbsp;: un acompte, puis une mensualité fixe pendant 12, 24 ou 36&nbsp;mois. Elle concerne l’Agaru Ultra et l’E-scooter 360. La Smart, elle, ne se loue pas en France.</li>
</ul>
<p>Le point qui change tout&nbsp;: en location, le <strong>service de réparation tout compris</strong> est inclus pour l’Agaru Ultra. Pneu crevé, frein usé, batterie fatiguée, accident&nbsp;: c’est pris en charge, et Augment vous envoie une trottinette de remplacement le temps de la réparation.</p>

<h2 id="le-calcul">Le calcul, sans détour</h2>
<p>Prenons l’Agaru Ultra, la plus louée de la gamme. Voici ce que vous payez au total selon la formule choisie (hors options comme la couverture vol à 2,95&nbsp;€/mois).</p>
<div class="art-table-wrap">
<table class="art-table">
 <caption>Coût total d’une Agaru Ultra selon la formule (tarifs augment.eco, France)</caption>
 <thead><tr><th scope="col">Formule</th><th scope="col">Acompte</th><th scope="col">Mensualité</th><th scope="col">Total payé</th></tr></thead>
 <tbody>
  <tr><th scope="row">Achat comptant</th><td>-</td><td>-</td><td><strong>549,00&nbsp;€</strong></td></tr>
  <tr><th scope="row">Location 12&nbsp;mois</th><td>399&nbsp;€</td><td>12,95&nbsp;€</td><td><strong>554,40&nbsp;€</strong></td></tr>
  <tr><th scope="row">Location 24&nbsp;mois</th><td>59&nbsp;€</td><td>32,95&nbsp;€</td><td>849,80&nbsp;€</td></tr>
  <tr><th scope="row">Location 36&nbsp;mois</th><td>399&nbsp;€</td><td>16,95&nbsp;€</td><td>1&nbsp;009,20&nbsp;€</td></tr>
  <tr><th scope="row">Location 36&nbsp;mois</th><td>59&nbsp;€</td><td>29,95&nbsp;€</td><td>1&nbsp;137,20&nbsp;€</td></tr>
  <tr><th scope="row">Crédit PayPal 24&nbsp;mois</th><td>-</td><td>26,59&nbsp;€</td><td>638,19&nbsp;€</td></tr>
 </tbody>
</table>
</div>
<p>Première surprise&nbsp;: sur 12&nbsp;mois avec un gros acompte, la location coûte à peine 5&nbsp;€ de plus que l’achat. Sauf que pendant cette année, vous n’avez rien à réparer de votre poche.</p>
<p>Deuxième constat, plus attendu&nbsp;: plus on étale, plus on paie. Sur trois ans, la location revient environ deux fois plus cher que l’achat comptant. C’est le prix de l’entretien inclus et d’un budget qui ne bouge pas.</p>
<aside class="tip"><p class="tip__t">Le conseil Roulelibre</p><p>Hésitant&nbsp;? Augment permet de retourner le véhicule dans les 14&nbsp;premiers jours de l’abonnement. Et à la fin, ou même en cours de route, vous pouvez racheter la trottinette en payant le solde restant. Louer n’empêche donc pas de devenir propriétaire plus tard.</p></aside>

<h2 id="louer-si">Louer, c’est fait pour vous si…</h2>
<ul class="check">
 <li>vous ne voulez pas sortir 549&nbsp;€ d’un coup&nbsp;;</li>
 <li>vous roulez tous les jours et une panne vous mettrait dans l’embarras (le remplacement est prévu)&nbsp;;</li>
 <li>vous n’avez ni le temps ni l’envie de changer une chambre à air&nbsp;;</li>
 <li>vous voulez tester la trottinette au quotidien avant de vous engager pour de bon&nbsp;;</li>
 <li>votre situation peut changer d’ici un an ou deux (déménagement, nouveau travail).</li>
</ul>

<h2 id="acheter-si">Acheter, c’est plus malin si…</h2>
<ul class="dash">
 <li>vous comptez la garder plusieurs années&nbsp;;</li>
 <li>vous êtes à l’aise avec l’entretien de base (pneus, freins)&nbsp;;</li>
 <li>vous visez l’Agaru Smart, proposée uniquement à l’achat (399&nbsp;€)&nbsp;;</li>
 <li>vous ne voulez aucun engagement de durée.</li>
</ul>

<h2 id="et-le-360">Et pour le scooter E-scooter 360&nbsp;?</h2>
<p>Même logique, autres montants. Le 360 coûte 1&nbsp;990&nbsp;€ à l’achat. En location, comptez par exemple 2&nbsp;112,80&nbsp;€ sur 12&nbsp;mois avec 1&nbsp;490&nbsp;€ d’acompte, ou 2&nbsp;422,40&nbsp;€ sur 36&nbsp;mois avec le même acompte. Attention à une différence de taille&nbsp;: le 360 n’a pas le service de réparation tout compris des Agaru. Il bénéficie d’une garantie constructeur de 2&nbsp;ans (5&nbsp;ans sur le cadre) et d’un service de pièces d’usure. On en parle dans notre <a href="scooter-electrique-pliable-45-km-h.html">guide du scooter pliable 45&nbsp;km/h</a>.</p>

<h2 id="employeur">Un coup de pouce de votre employeur&nbsp;?</h2>
<p>Si votre entreprise propose le forfait mobilités durables, une partie de vos frais de trottinette (achat ou location) peut être prise en charge, sans impôt ni cotisations jusqu’à un certain plafond. Ce n’est pas automatique&nbsp;: l’employeur décide s’il le propose et à quel montant. Renseignez-vous auprès de votre service RH, et lisez notre <a href="forfait-mobilites-durables-trottinette-electrique.html">guide du forfait mobilités durables</a>.</p>
''',
 cta=dict(titre='Faites le calcul avec votre budget', texte='Le simulateur reprend la grille réelle d’Augment&nbsp;: choisissez la durée, l’acompte et les options, et voyez la mensualité tout de suite.',
          boutons=['<a class="btn btn--primary" href="../configurateur.html?model=ultra">Simuler ma location <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(ULTRA, 'Voir l’Agaru Ultra sur augment.eco')]),
 faq=[
  ('Est-ce moins cher de louer ou d’acheter une trottinette électrique ?', 'Sur 12 mois avec l’acompte maximal, le coût d’une Agaru Ultra en location (554,40 €) est quasi identique au prix d’achat (549 €), réparations comprises. Sur 24 ou 36 mois, la location revient plus cher que l’achat comptant.'),
  ('Peut-on acheter la trottinette à la fin de la location ?', 'Oui. Augment propose une option d’achat à la fin de l’abonnement, ou à tout moment en payant le solde restant.'),
  ('La location d’une trottinette Augment comprend-elle les réparations ?', 'Pour l’Agaru Ultra, oui : le service tout compris couvre les pannes, l’usure, les accidents, la batterie, les freins et les pneus, avec une trottinette de remplacement. Pour l’E-scooter 360, la garantie constructeur et un service de pièces d’usure s’appliquent.'),
 ],
 sources=[('Tarifs, durées et acomptes : tunnel de commande augment.eco (France)', 'https://augment.eco/fr-fr/agaru-ultra/'), ('Essai 14 jours et option d’achat : FAQ augment.eco', 'https://augment.eco/fr-fr/agaru-smart/')],
 lies=['forfait-mobilites-durables-trottinette-electrique', 'trottinette-electrique-volee-que-faire', 'agaru-smart-ou-agaru-ultra-difference'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='trottinette-electrique-assurance-reglementation',
 categorie='Règles et assurance',
 titre_seo='Trottinette électrique : assurance obligatoire et règles 2026',
 description='Assurance, âge minimum, casque, trottoir, amendes : tout ce qu’il faut savoir pour rouler en trottinette électrique en règle en 2026, expliqué simplement.',
 h1='Trottinette électrique&nbsp;: les règles pour rouler tranquille en 2026.',
 chapo='Assurance, âge, casque, trottoir, écouteurs… Les règles ont pas mal bougé ces dernières années. Voici l’essentiel, sans jargon, pour rouler l’esprit léger et éviter les mauvaises surprises.',
 image=('art-regles-piste', 'Piste cyclable mouillée en fin de journée, panneau bleu de piste obligatoire et une personne casquée en trottinette électrique au loin'),
 lecture=5,
 en_bref=[
  'L’assurance responsabilité civile est obligatoire. Sans elle, l’amende peut monter jusqu’à 3&nbsp;750&nbsp;€.',
  'Il faut avoir au moins 14&nbsp;ans, et la vitesse est limitée à 25&nbsp;km/h.',
  'Interdit&nbsp;: rouler à deux, porter des écouteurs, tenir son téléphone, rouler sur le trottoir.',
  'Le casque est obligatoire hors agglomération, et vivement conseillé en ville.',
 ],
 corps='''
<h2 id="assurance">L’assurance&nbsp;: obligatoire, et pas chère</h2>
<p>C’est la règle qu’on oublie le plus souvent. Une trottinette électrique est un engin motorisé&nbsp;: comme une voiture ou un scooter, elle doit être couverte par une <strong>assurance responsabilité civile</strong>. Elle paie les dégâts que vous pourriez causer à quelqu’un d’autre. Selon la Sécurité routière, ce type de contrat coûte en général 2 ou 3&nbsp;euros par mois.</p>
<p>Rouler sans assurance expose à une amende pouvant atteindre <strong>3&nbsp;750&nbsp;€</strong>. Et surtout, en cas d’accident, les frais seraient pour vous.</p>
<aside class="tip"><p class="tip__t">À ne pas confondre</p><p>La couverture contre le vol proposée par Augment (2,95&nbsp;€/mois) protège votre trottinette contre le vol, la perte et le vandalisme. Elle ne remplace pas la responsabilité civile. Pensez à vérifier votre contrat habitation&nbsp;: certains incluent déjà les engins de déplacement personnels, d’autres non.</p></aside>

<h2 id="qui">Qui peut rouler, et à quelle vitesse&nbsp;?</h2>
<p>Depuis le décret du 31&nbsp;août 2023, il faut avoir <strong>au moins 14&nbsp;ans</strong> (c’était 12 avant). Un enfant plus jeune au guidon, c’est 135&nbsp;€ d’amende.</p>
<p>La vitesse maximale est de <strong>25&nbsp;km/h</strong>. Les Agaru Smart et Ultra d’Augment sont bridées à cette vitesse&nbsp;: aucun réglage à faire de votre côté.</p>

<h2 id="ou">Où a-t-on le droit de rouler&nbsp;?</h2>
<ul>
 <li><strong>En ville</strong>&nbsp;: sur les pistes et bandes cyclables quand il y en a. Sinon, sur les routes limitées à 50&nbsp;km/h.</li>
 <li><strong>Hors agglomération</strong>&nbsp;: sur les voies vertes et pistes cyclables. Les routes ne sont autorisées que si le maire ou le préfet l’a prévu, et alors casque, équipement réfléchissant et feux allumés sont obligatoires.</li>
 <li><strong>Sur le trottoir</strong>&nbsp;: non, sauf autorisation locale. Si vous devez emprunter un trottoir, descendez et marchez à côté.</li>
</ul>

<h2 id="interdits">Les interdits à connaître</h2>
<ul class="dash">
 <li>Rouler à deux&nbsp;: la trottinette est strictement individuelle.</li>
 <li>Porter des écouteurs ou un casque audio, même d’un seul côté.</li>
 <li>Tenir son téléphone en roulant.</li>
 <li>Rouler dans les aires piétonnes ou à contresens&nbsp;: 135&nbsp;€ d’amende.</li>
</ul>
<figure class="art-fig">
 <img src="../img/conseils/art-regles-casque.webp" srcset="../img/conseils/art-regles-casque-800.webp 800w, ../img/conseils/art-regles-casque.webp 1536w" sizes="(max-width: 760px) 92vw, 720px" width="1536" height="1024" alt="Un casque de vélo accroché au portemanteau d’une entrée d’appartement, près des clés et des baskets" loading="lazy" decoding="async">
 <figcaption>Accroché près de la porte, on ne l’oublie pas&nbsp;: le casque reste le bon réflexe, même pour un trajet court.</figcaption>
</figure>

<h2 id="equipement">L’équipement de la trottinette</h2>
<p>Une trottinette électrique doit avoir des feux avant et arrière, des catadioptres, un système de freinage et un avertisseur sonore. Bonne nouvelle&nbsp;: les modèles vendus en magasin les ont déjà. L’Agaru d’Augment ajoute des clignotants intégrés aux poignées et un double système de freinage, bien utiles en ville.</p>

<h2 id="casque">Et le casque, alors&nbsp;?</h2>
<p>En ville, il n’est pas obligatoire. Hors agglomération, il l’est. Notre avis&nbsp;: portez-le tout le temps. À 25&nbsp;km/h, une chute sur la tête n’a rien d’anodin. Augment propose d’ailleurs un casque Alpina Soho à 39&nbsp;€ lors de la commande.</p>
''',
 cta=dict(titre='Une trottinette déjà équipée pour la ville', texte='Feux, clignotants, double freinage, étanchéité IPX5&nbsp;: comparez les deux Agaru et le scooter 360 critère par critère.',
          boutons=['<a class="btn btn--primary" href="../comparateur.html">Voir le comparatif <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(ULTRA, 'Voir l’Agaru sur augment.eco')]),
 faq=[
  ('L’assurance est-elle obligatoire pour une trottinette électrique ?', 'Oui. Une trottinette électrique doit être couverte par une assurance responsabilité civile. Rouler sans assurance expose à une amende pouvant atteindre 3 750 €.'),
  ('À partir de quel âge peut-on conduire une trottinette électrique ?', 'À partir de 14 ans, depuis le décret n° 2023-848 du 31 août 2023. Avant, l’âge minimum était de 12 ans.'),
  ('Le casque est-il obligatoire en trottinette électrique ?', 'Il est obligatoire hors agglomération, quand la circulation y est autorisée. En ville, il n’est pas obligatoire mais fortement recommandé.'),
  ('Peut-on rouler sur le trottoir en trottinette électrique ?', 'Non, sauf autorisation locale. Sur un trottoir, il faut descendre et marcher à côté de la trottinette.'),
 ],
 sources=[('Sécurité routière : réglementation des engins de déplacement personnels motorisés', 'https://www.securite-routiere.gouv.fr/reglementation-liee-aux-modes-de-deplacements/reglementation-des-edpm'),
          ('Sécurité routière : obligation d’assurer les EDPM', 'https://www.securite-routiere.gouv.fr/actualites/une-campagne-radio-rappelle-lobligation-dassurer-les-engins-de-deplacement-personnels'),
          ('Code Rousseau : trottinette électrique et code de la route en 2026', 'https://public.codesrousseau.fr/conseils-pratiques/473-trottinette-electrique-reglementation-et-code-de-la-route-en-2026-edpm.html')],
 lies=['trottinette-electrique-volee-que-faire', 'rouler-sous-la-pluie-trottinette-electrique', 'prendre-le-train-avec-sa-trottinette-electrique'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='trottinette-electrique-ecologique',
 categorie='Écologie',
 titre_seo='La trottinette électrique est-elle vraiment écologique ?',
 description='Bilan carbone, fabrication, batterie, durée de vie : le point honnête sur l’impact d’une trottinette électrique, et ce qui la rend vraiment plus verte.',
 h1='La trottinette électrique est-elle vraiment écologique&nbsp;?',
 chapo='Pas de pot d’échappement, pas de bruit… mais une batterie et de l’aluminium à fabriquer. Alors, vraiment plus verte que la voiture&nbsp;? La réponse est oui, à une condition&nbsp;: la garder longtemps.',
 image=('art-ecologie-rue', 'Rue arborée au printemps avec piste cyclable, ligne de tram, cyclistes et piétons'),
 lecture=5,
 en_bref=[
  'L’essentiel de l’impact d’une trottinette vient de sa fabrication, pas de l’électricité qu’elle consomme.',
  'Les trottinettes en libre-service, renouvelées vite et collectées en camionnette, ont un bilan médiocre&nbsp;: environ 105&nbsp;g de CO₂ par km et par usager selon une étude menée à Paris.',
  'Une trottinette personnelle gardée plusieurs années et bien entretenue s’approche du bilan des transports en commun.',
  'Réparer plutôt que remplacer&nbsp;: c’est là que se joue vraiment l’écologie.',
 ],
 corps='''
<h2 id="ou-est-l-impact">Où se cache l’impact d’une trottinette&nbsp;?</h2>
<p>On pense souvent à l’électricité. En réalité, recharger une trottinette ne pèse presque rien, surtout en France où l’électricité est peu carbonée. Dans l’étude sur les trottinettes en libre-service à Paris, la recharge ne représente que 2,4&nbsp;% des émissions.</p>
<p>Le gros du bilan, c’est la <strong>fabrication</strong>&nbsp;: le cadre en aluminium, le moteur et surtout la batterie lithium-ion. Dans cette même étude, matériaux et fabrication pèsent plus de la moitié des émissions (57,4&nbsp;%). Le reste vient en grande partie de la collecte des trottinettes pour les recharger, en camionnette.</p>

<h2 id="libre-service">Le libre-service, mauvais élève</h2>
<p>Les trottinettes partagées ont eu une vie courte et un entretien coûteux en kilomètres de camionnette. Résultat&nbsp;: un peu plus de <strong>105&nbsp;g d’équivalent CO₂ par kilomètre et par usager</strong> sur leur cycle de vie, selon l’étude menée à Paris. C’est à peu près le niveau d’une voiture où l’on serait trois à bord.</p>

<h2 id="personnelle">Une trottinette à soi, c’est une autre histoire</h2>
<p>Avec une trottinette personnelle, pas de camionnette qui tourne la nuit pour la recharger. Et surtout, on la garde. Une trottinette personnelle bien entretenue peut parcourir environ 15&nbsp;000&nbsp;km&nbsp;: la pollution de sa fabrication est alors répartie sur beaucoup plus de trajets. Son bilan devient comparable à celui des transports en commun à Paris, et meilleur dans la plupart des autres villes.</p>
<p>Pour comparer, l’ADEME estime l’usage d’une voiture thermique à près de 200&nbsp;g d’équivalent CO₂ par kilomètre. Remplacer quelques trajets en voiture par la trottinette, c’est donc un vrai geste, à condition de ne pas la changer tous les ans.</p>
<figure class="art-fig">
 <img src="../img/conseils/art-ecologie-tram.webp" srcset="../img/conseils/art-ecologie-tram-800.webp 800w, ../img/conseils/art-ecologie-tram.webp 1536w" sizes="(max-width: 760px) 92vw, 720px" width="1536" height="1024" alt="Sur un quai de tram, une jeune femme attend avec sa trottinette électrique pliée à la main" loading="lazy" decoding="async">
 <figcaption>Pliée en quelques secondes, elle monte dans le tram ou le train&nbsp;: idéal pour les trajets mixtes.</figcaption>
</figure>

<h2 id="durer">Faire durer sa trottinette&nbsp;: le vrai geste vert</h2>
<p>Puisque tout se joue sur la durée de vie, ce qui compte, c’est de <strong>pouvoir réparer</strong>. Une trottinette dont on ne trouve pas les pièces finit à la benne au premier pépin.</p>
<p>C’est le parti pris d’Augment avec ses Agaru&nbsp;: un service de réparation qui prend en charge l’usure, les pannes, les freins, les pneus et la batterie. En cas de vol couvert, la trottinette est remplacée par un modèle reconditionné. Pour le scooter 360, la batterie est amovible et des pièces d’usure sont disponibles.</p>
<aside class="tip"><p class="tip__t">Nos trois réflexes</p><p>Gonfler les pneus régulièrement (à froid), ne pas laisser la batterie à plat pendant des semaines, et la ranger au sec. Trois gestes simples qui prolongent sa vie, et donc son bénéfice pour la planète.</p></aside>

<h2 id="combiner">Et si on combinait&nbsp;?</h2>
<p>La trottinette n’a pas vocation à tout remplacer. Elle brille sur les 2 à 10&nbsp;km du quotidien, et en complément du train ou du tram pour le premier et le dernier kilomètre. C’est souvent là qu’on lâche la voiture pour de bon.</p>
''',
 cta=dict(titre='Une trottinette pensée pour durer', texte='Réparations comprises en location, batterie fixe protégée dans le plateau, étanchéité IPX5&nbsp;: découvrez l’Agaru et simulez votre location.',
          boutons=['<a class="btn btn--primary" href="../configurateur.html?model=ultra">Simuler ma location <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(ULTRA, 'Voir l’Agaru Ultra sur augment.eco')]),
 faq=[
  ('Une trottinette électrique pollue-t-elle moins qu’une voiture ?', 'Oui, si elle est gardée longtemps. Une trottinette personnelle bien entretenue a un bilan proche des transports en commun, alors que l’usage d’une voiture thermique est estimé à près de 200 g d’équivalent CO₂ par kilomètre.'),
  ('Qu’est-ce qui pollue le plus dans une trottinette électrique ?', 'Sa fabrication, en particulier la batterie et le cadre en aluminium. La recharge ne représente qu’une petite part des émissions.'),
  ('Pourquoi les trottinettes en libre-service sont-elles moins écologiques ?', 'Elles ont une durée de vie courte et doivent être collectées en camionnette pour être rechargées. Une étude menée à Paris a estimé leur bilan à un peu plus de 105 g d’équivalent CO₂ par kilomètre et par usager.'),
 ],
 sources=[('Étude sur l’impact des trottinettes en libre-service (relayée par Connaissance des Énergies, AFP)', 'https://www.connaissancedesenergies.org/afp/la-trottinette-en-libre-service-doit-encore-prouver-quelle-est-ecologique-190705'),
          ('ADEME : calculer les émissions de carbone de vos trajets', 'https://agirpourlatransition.ademe.fr/particuliers/evaluer-son-impact/calculer-empreinte-carbone/calculer-emissions-carbone-trajets'),
          ('Service de réparation et couverture vol : augment.eco', 'https://augment.eco/fr-fr/')],
 lies=['batterie-trottinette-electrique-duree-de-vie', 'prendre-le-train-avec-sa-trottinette-electrique', 'trottinette-ou-scooter-electrique-choisir'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='scooter-electrique-pliable-45-km-h',
 categorie='Scooter 45 km/h',
 titre_seo='Scooter électrique pliable 45 km/h : permis et assurance',
 description='Permis AM, carte grise, assurance, casque, rangement en appartement : le guide simple du scooter électrique pliable 45 km/h, avec l’E-scooter 360.',
 h1='Scooter électrique pliable 45&nbsp;km/h&nbsp;: le guide simple.',
 chapo='Plus rapide qu’une trottinette, plus compact qu’un scooter classique&nbsp;: le scooter pliable à 45&nbsp;km/h a tout pour plaire en ville. Mais ce n’est plus un simple engin de déplacement&nbsp;: permis, carte grise et équipement entrent en jeu. On vous explique.',
 image=('art-scooter-stationnement', 'Scooters et cyclomoteurs garés sur un emplacement deux-roues dans une rue en ville'),
 lecture=6,
 en_bref=[
  'Un scooter électrique à 45&nbsp;km/h est un cyclomoteur (catégorie L1e)&nbsp;: ce n’est pas une trottinette.',
  'Il faut le permis AM (ex-BSR) ou le permis B, une carte grise et une assurance de véhicule motorisé.',
  'Casque homologué et gants homologués sont obligatoires.',
  'L’E-scooter 360 d’Augment se plie et se range chez vous&nbsp;: 1&nbsp;265 × 350 × 1&nbsp;180&nbsp;mm une fois plié.',
 ],
 corps='''
<h2 id="pas-une-trottinette">Ce n’est pas une trottinette (et c’est important)</h2>
<p>Dès qu’un véhicule électrique dépasse 25&nbsp;km/h et monte jusqu’à 45&nbsp;km/h, il change de famille&nbsp;: c’est un <strong>cyclomoteur</strong>, catégorie L1e. Les règles des trottinettes ne s’appliquent plus. On passe à celles des scooters 50&nbsp;cm³.</p>
<p>La bonne nouvelle&nbsp;: à 45&nbsp;km/h, vous roulez dans le trafic, sur la chaussée, sans vous faire doubler par tout le monde. Idéal pour des trajets de 10 à 20&nbsp;km.</p>

<h2 id="permis">Quel permis faut-il&nbsp;?</h2>
<p>Il faut le <strong>permis AM</strong> (l’ancien BSR), accessible dès 14&nbsp;ans après une formation courte, ou le <strong>permis B</strong> si vous conduisez déjà une voiture. Les personnes nées avant le 1<sup>er</sup>&nbsp;janvier 1988 en sont dispensées pour un cyclomoteur.</p>

<h2 id="papiers">Carte grise et assurance</h2>
<p>Comme tout scooter, un cyclomoteur électrique doit être <strong>immatriculé</strong>. La démarche se fait en ligne sur le site de l’ANTS. Une plaque se fixe à l’arrière&nbsp;: l’E-scooter 360 a un support prévu pour.</p>
<p>Il faut aussi une <strong>assurance de véhicule motorisé</strong>, au minimum la responsabilité civile. Demandez des devis&nbsp;: les tarifs varient beaucoup selon votre profil et votre ville.</p>

<h2 id="equipement">Casque et gants&nbsp;: non négociables</h2>
<p>Le <strong>casque homologué</strong> et les <strong>gants homologués</strong> sont obligatoires, été comme hiver. À 45&nbsp;km/h, ce n’est pas du luxe.</p>
<figure class="art-fig">
 <img src="../img/conseils/art-scooter-equipement.webp" srcset="../img/conseils/art-scooter-equipement-800.webp 800w, ../img/conseils/art-scooter-equipement.webp 1536w" sizes="(max-width: 760px) 92vw, 720px" width="1536" height="1024" alt="Un casque jet et des gants en cuir posés sur un banc dans l’entrée, prêts pour un trajet en scooter électrique" loading="lazy" decoding="async">
 <figcaption>Casque et gants&nbsp;: obligatoires à chaque trajet sur un scooter 45&nbsp;km/h.</figcaption>
</figure>

<h2 id="ranger">Le vrai plus du pliable&nbsp;: le rangement</h2>
<p>Pas de garage, pas de local à vélos&nbsp;? C’est là que le scooter pliable prend tout son sens. L’E-scooter 360 d’Augment se replie à <strong>1&nbsp;265 × 350 × 1&nbsp;180&nbsp;mm</strong>. Il entre dans un ascenseur, se glisse dans une entrée ou au bureau. Il pèse 36&nbsp;kg batterie comprise&nbsp;: on le roule plus qu’on ne le porte.</p>
<p>Sa batterie de 1&nbsp;080&nbsp;Wh est <strong>amovible</strong>&nbsp;: vous pouvez la monter chez vous pour la recharger, même si le scooter reste en bas. Avec une seconde batterie en option, l’autonomie passe de 53 à 106&nbsp;km.</p>
<aside class="tip"><p class="tip__t">Le conseil Roulelibre</p><p>Avant de choisir, mesurez votre ascenseur et votre entrée. 35&nbsp;cm de large une fois plié, c’est très compact, mais mieux vaut vérifier que ça passe la porte de l’ascenseur.</p></aside>

<h2 id="combien">Combien ça coûte&nbsp;?</h2>
<p>L’E-scooter 360 coûte 1&nbsp;990&nbsp;€ à l’achat, ou se loue dès 25,90&nbsp;€/mois sur 36&nbsp;mois avec 1&nbsp;490&nbsp;€ d’acompte (de 64,90 à 159,90&nbsp;€/mois avec l’acompte minimal de 290&nbsp;€, selon la durée). Contrairement aux Agaru, il n’inclut pas le service de réparation tout compris&nbsp;: il est couvert par une garantie constructeur de 2&nbsp;ans, 5&nbsp;ans sur le cadre. On compare les formules dans <a href="louer-ou-acheter-trottinette-electrique.html">louer ou acheter&nbsp;: le match</a>.</p>
''',
 cta=dict(titre='Le 360 en détail', texte='Autonomie, poids, dimensions plié, grille de location complète&nbsp;: tout est dans la fiche et le simulateur.',
          boutons=['<a class="btn btn--primary" href="../configurateur.html?model=360">Simuler le 360 <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(S360, 'Voir le 360 sur augment.eco')]),
 faq=[
  ('Quel permis pour un scooter électrique 45 km/h ?', 'Le permis AM (ex-BSR) ou le permis B. Les personnes nées avant le 1er janvier 1988 en sont dispensées pour un cyclomoteur.'),
  ('Un scooter électrique pliable doit-il être immatriculé ?', 'Oui. Un scooter électrique qui roule jusqu’à 45 km/h est un cyclomoteur (catégorie L1e) : il doit avoir une carte grise, une plaque et une assurance.'),
  ('Le casque et les gants sont-ils obligatoires sur un scooter électrique ?', 'Oui. Le casque homologué et les gants homologués sont obligatoires sur un cyclomoteur, donc sur un scooter électrique à 45 km/h.'),
  ('Quelles sont les dimensions de l’E-scooter 360 plié ?', '1 265 × 350 × 1 180 mm, pour un poids de 36 kg batterie comprise, selon Augment.'),
 ],
 sources=[('Caractéristiques et prix de l’E-scooter 360 : augment.eco (France)', 'https://augment.eco/fr-fr/augment-360/'),
          ('Immatriculation d’un véhicule : ANTS', 'https://immatriculation.ants.gouv.fr/'),
          ('Que Choisir : le speed bike, un cyclomoteur à pédales (règles L1e)', 'https://www.quechoisir.org/decryptage-velo-electrique-le-speed-bike-un-cyclomoteur-a-pedale-n89126/')],
 lies=['trottinette-ou-scooter-electrique-choisir', 'forfait-mobilites-durables-trottinette-electrique', 'trottinette-electrique-assurance-reglementation'],
),

# ---------------------------------------------------------------------------------------------
dict(
 slug='trottinette-electrique-volee-que-faire',
 categorie='Sécurité',
 titre_seo='Trottinette électrique volée : les 4 étapes d’urgence',
 description='Votre trottinette a disparu ? Les 4 réflexes immédiats : blocage à distance dans l’application, plainte, déclaration d’assurance et franchise de remplacement.',
 h1='Trottinette électrique volée&nbsp;: que faire dans l’heure qui suit&nbsp;?',
 chapo='C’est la mauvaise surprise que tout le monde redoute en sortant d’un magasin ou de son travail. Votre trottinette n’est plus là où vous l’aviez attachée. Pas de panique : voici les démarches exactes à mener, étape par étape, pour tenter de la localiser et faire jouer vos garanties sans perdre de temps.',
 image=('regles-trottinette-soir', 'Une trottinette électrique stationnée le soir sur un trottoir urbain bien éclairé'),
 anim=False,
 lecture=5,
 en_bref=[
  'Verrouillez immédiatement le moteur depuis votre application mobile pour la rendre inutilisable.',
  'Déposez plainte sous 24 à 48 heures au commissariat ou via la pré-plainte en ligne avec votre numéro de série.',
  'Déclarez le sinistre à votre assurance ou auprès de votre loueur dans les 2 jours ouvrés.',
  'Avec l’option vol Augment (2,95 €/mois), vous recevez une nouvelle trottinette contre une franchise de 100 à 150 €.',
 ],
 corps='''
<h2 id="blocage-immediat">1. Bloquer la trottinette à distance dans l’application</h2>
<p>Dès le constat de la disparition, ouvrez l’application mobile connectée à votre trottinette. Chez Augment, l’application permet de <strong>verrouiller électroniquement le moteur</strong> à distance. Une trottinette verrouillée résiste au roulement et devient totalement inerte : impossible de l’allumer ou de repartir avec l’assistance électrique.</p>
<p>Cette manipulation empêche le voleur de s’en servir immédiatement et décourage la revente à la sauvette auprès d’un particulier.</p>

<h2 id="depot-plainte">2. Déposer plainte auprès de la police ou de la gendarmerie</h2>
<p>Le dépôt de plainte est un préalable légal indispensable pour faire jouer n’importe quelle assurance ou garantie. Vous disposez généralement de <strong>24 à 48 heures</strong> après le vol.</p>
<p>Pour gagner du temps, commencez par remplir une <strong>pré-plainte en ligne</strong> sur le site officiel du ministère de l’Intérieur. Rendez-vous ensuite au commissariat pour signer le procès-verbal. N’oubliez pas de vous munir des éléments suivants :</p>
<ul class="check">
 <li>votre <strong>pièce d’identité</strong> ;</li>
 <li>le <strong>numéro de série</strong> exact du châssis (noté sur votre contrat de location ou votre facture d’achat) ;</li>
 <li>une photo du véhicule et, si vous l’avez, le numéro d’identification national gravé (marquage Paravol ou Bicycode) ;</li>
 <li>la facture de l’antivol utilisé et une photo du point fixe où elle était attachée si l’antivol a été sectionné.</li>
</ul>

<h2 id="declaration-assurance">3. Déclarer le vol à votre assurance ou à votre loueur</h2>
<p>Vous devez contacter votre assureur dans un délai strict de <strong>2 jours ouvrés</strong> après la découverte du vol en transmettant le récépissé de dépôt de plainte.</p>
<p>La prise en charge dépend directement de votre contrat :</p>
<ul class="dash">
 <li><strong>Si vous avez acheté votre trottinette</strong> : votre assurance responsabilité civile obligatoire ne couvre pas le vol. Seule une garantie spécifique « vol et dommages » (optionnelle, de 5 à 15 €/mois) ou une extension de votre multirisque habitation avec option villégiature interviendra, souvent avec une vétusté importante et une franchise de 100 à 300 €.</li>
 <li><strong>Si vous louez chez Augment</strong> : avec l’option couverture vol à <strong>2,95 € par mois</strong>, vous êtes protégé en cas de vol avec effraction d’un antivol homologué. Après validation du dossier de plainte, Augment vous expédie une trottinette de remplacement contre le paiement d’une franchise forfaitaire (100 € pour l’Agaru Smart, 150 € pour l’Agaru Ultra).</li>
 </ul>
<aside class="tip"><p class="tip__t">Attention à la règle de l’antivol</p><p>Pour que la couverture vol fonctionne, que ce soit chez un assureur ou chez un loueur, votre trottinette doit obligatoirement avoir été attachée à un point fixe à l’aide d’un antivol en U ou pliant homologué (vendu ou certifié par la marque). Un simple câble fin en spirale entraîne presque systématiquement un refus de prise en charge.</p></aside>

<h2 id="eviter-recidive">4. Trois habitudes simples pour éviter que ça ne recommence</h2>
<p>La majorité des vols ont lieu lors d’un arrêt rapide de moins de dix minutes sans attache à un point fixe. Pour rouler l’esprit tranquille :</p>
<ol>
 <li><strong>Ne laissez jamais la trottinette seule dans la rue la nuit.</strong> En rentrant chez vous, pliez-la et rentrez-la dans votre entrée ou votre garage fermé.</li>
 <li><strong>Attachez toujours le cadre, jamais une roue amovible.</strong> Sur l’Agaru, passez l’antivol en U rigide autour du tube de potence inférieur ou du renfort de châssis, solidement accroché à un arceau en acier scellé dans le béton.</li>
 <li><strong>Préférez les parkings vélos surveillés ou sécurisés.</strong> Les abris vélos de gare accessibles avec un pass de transport réduisent de plus de 80 % le risque d’effraction.</li>
</ol>
''',
 cta=dict(titre='Roulez sans la peur du vol', texte='Découvrez comment fonctionne la couverture vol à 2,95 €/mois et le remplacement rapide en cas de pépin sur l’Agaru Ultra.',
          boutons=['<a class="btn btn--primary" href="../comparateur.html#assurance">Comparer les garanties <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(ULTRA, 'Voir l’Agaru Ultra sur augment.eco')]),
 faq=[
  ('Que faire immédiatement après le vol de sa trottinette électrique ?', 'Verrouillez le moteur à distance depuis l’application mobile, remplissez une pré-plainte en ligne avec le numéro de série, puis déclarez le vol à votre assurance ou loueur sous 2 jours ouvrés.'),
  ('Une assurance trottinette électrique couvre-t-elle toujours le vol ?', 'Non. L’assurance responsabilité civile obligatoire ne couvre que les dégâts causés aux tiers. Pour être indemnisé du véhicule, il faut souscrire une garantie vol spécifique ou une option tranquillité auprès de votre loueur.'),
  ('Quel est le montant de la franchise vol chez Augment ?', 'Avec l’option vol à 2,95 €/mois, la franchise s’élève à 100 € pour une Agaru Smart et à 150 € pour une Agaru Ultra, sous réserve d’avoir déposé plainte et utilisé un antivol homologué.'),
  ('Comment retrouver une trottinette électrique volée ?', 'Vérifiez les sites de petites annonces locales (Leboncoin, Facebook Marketplace) avec la marque et le modèle, transmettez les alertes à la police et surveillez les réseaux de revente sans jamais intervenir seul.'),
 ],
 sources=[('Démarche de pré-plainte en ligne du ministère de l’Intérieur', 'https://www.pre-plainte-en-ligne.gouv.fr/'),
          ('Conditions générales et couverture vol : help.augment.eco/fr', 'https://help.augment.eco/fr/articles/6462725-que-faire-en-cas-de-vol'),
          ('Guide de prévention du vol de deux-roues : FUB (Fédération française des usagers de la bicyclette)', 'https://www.fub.fr/antivols')],
 lies=['trottinette-electrique-assurance-reglementation', 'louer-ou-acheter-trottinette-electrique', 'rouler-sous-la-pluie-trottinette-electrique'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='rouler-sous-la-pluie-trottinette-electrique',
 categorie='Pratique',
 titre_seo='Trottinette électrique sous la pluie : IPX5 et conseils',
 description='Peut-on rouler sous la pluie en trottinette électrique ? Comprendre l’indice IPX5, éviter les glissades, freiner court et bien sécher votre engin.',
 h1='Rouler sous la pluie en trottinette électrique&nbsp;: ce qui est permis, ce qui est risqué',
 chapo='L’automne et l’hiver n’épargnent personne : tôt ou tard, vous allez croiser des averses sur votre trajet. Est-ce dangereux pour l’électronique ? Vos pneus tiennent-ils la route ? Voici les règles indispensables pour rouler en toute sécurité sans abîmer votre matériel.',
 image=('art-regles-piste', 'Une piste cyclable mouillée bordée de pavés par temps de pluie automnale'),
 anim=False,
 lecture=6,
 en_bref=[
  'L’indice IPX5 (Agaru) résiste très bien aux jets d’eau et aux fortes averses, mais interdit formellement l’immersion dans les flaques profondes.',
  'Sur sol mouillé, la distance de freinage est multipliée par deux : anticipez et utilisez le frein arrière avant le frein avant.',
  'Les pneus gonflables 10 pouces absorbent l’eau ; les pneus pleins sans air sont de véritables patinoires sur bandes blanches.',
  'En arrivant, essuyez le châssis avec un chiffon sec et ne branchez jamais le chargeur sur un connecteur humide.',
 ],
 corps='''
<h2 id="indice-ipx5">Que signifie l’étanchéité IPX5&nbsp;?</h2>
<p>Toutes les trottinettes électriques ne sont pas égales face à l’eau. Beaucoup de modèles d’entrée de gamme n’affichent qu’une certification IPX4 (résistance aux éclaboussures légères). L’Agaru d’Augment bénéficie d’un indice <strong>IPX5</strong> sur l’ensemble de sa structure.</p>
<p>Concrètement :</p>
<ul class="check">
 <li><strong>Ce qui est couvert :</strong> rouler sous une pluie battante continue, les projections d’eau soulevées par la roue avant et le nettoyage au jet d’eau basse pression sans solvant.</li>
 <li><strong>Ce qui est interdit :</strong> plonger la trottinette dans une flaque dont le niveau dépasse le bas du plateau, l’immersion totale ou l’utilisation d’un nettoyeur haute pression (Kärcher) qui forcerait les joints des roulements de roue.</li>
 </ul>
<p>La batterie de l’Agaru étant logée dans le plateau aluminium sous un joint hermétique, elle ne craint pas l’eau ruisselante du dessus. Mais traverser une flaque de 10 centimètres de profondeur reste le meilleur moyen d’endommager le contrôleur moteur.</p>

<h2 id="adherence-freinage">Adhérence et freinage : adapter sa conduite</h2>
<p>Sur route mouillée, le coefficient d’adhérence du bitume chute de plus de 40 %. À 25 km/h, votre distance d’arrêt passe d’environ 3,5 mètres sur sol sec à <strong>plus de 6 mètres</strong> sur sol détrempé.</p>
<p>Deux pièges urbains provoquent 9 chutes sur 10 sous la pluie :</p>
<ol>
 <li><strong>Le marquage au sol et les plaques d’égout :</strong> les bandes blanches piétonnes, les résines vertes cyclables et les plaques en fonte deviennent de vraies patinoires au contact de l’eau. Traversez-les toujours en ligne droite, sans freiner ni tourner le guidon.</li>
 <li><strong>Les feuilles mortes mouillées :</strong> elles créent un tapis glissant imperceptible qui bloque la direction au moindre virage appuyé.</li>
</ol>
<p>Côté freinage, le système de l’Agaru combine un <strong>frein à disque mécanique arrière</strong> et un <strong>frein moteur eABS avant</strong>. Sous la pluie, dosez d’abord la poignée pour engager le frein arrière et asseoir le véhicule, puis complétez doucement avec l’avant pour ne pas bloquer la roue directrice.</p>

<figure class="art-fig">
 <img src="../img/conseils/guide-frein-arriere.webp" srcset="../img/conseils/guide-frein-arriere-800.webp 800w, ../img/conseils/guide-frein-arriere.webp 1536w" sizes="(max-width: 760px) 92vw, 720px" width="1536" height="1024" alt="Gros plan sur le disque de frein mécanique arrière et le pneu 10 pouces d’une trottinette électrique" loading="lazy" decoding="async">
 <figcaption>Le frein à disque mécanique arrière garantit un freinage progressif et puissant, même sous la pluie.</figcaption>
</figure>

<h2 id="pression-pneus">Pneus à air vs pneus pleins : la différence vitale</h2>
<p>L’Agaru Smart et l’Agaru Ultra sont équipées de <strong>pneus de 10 × 2,5 pouces avec chambre à air</strong>. C’est un choix technique décisif pour l’hiver : la gomme souple et la déformation naturelle de l’air épousent les micro-aspérités de la route et évacuent l’eau grâce aux rainures.</p>
<p>À l’inverse, les trottinettes à pneus pleins en gomme rigide (souvent vantées pour ne jamais crever) n’ont aucune adhérence sur chaussée humide : la surface de contact est minuscule et le pneu glisse au moindre freinage d’urgence.</p>
<aside class="tip"><p class="tip__t">L’astuce pression pour l’hiver</p><p>Sur sol sec, la pression recommandée est de 3,5 bars (50 PSI). En période de pluies régulières ou sur chaussée grasse, baisser la pression à <strong>3,1 ou 3,2 bars</strong> élargit la bande de roulement de 15 % et améliore considérablement le grip sans risquer de pincer la chambre à air.</p></aside>

<h2 id="entretien-retour">Que faire en arrivant chez soi&nbsp;?</h2>
<ul class="dash">
 <li><strong>Passez un coup de microfibre sec</strong> sur l’écran LED, les poignées et le plateau pour retirer l’eau résiduelle et le sel de déneigement en hiver.</li>
 <li><strong>Vérifiez le cache en caoutchouc du port de charge</strong> situé sur le côté du plateau : il doit être parfaitement fermé et hermétique.</li>
 <li><strong>Attendez au moins 30 minutes avant de brancher le chargeur</strong> si le véhicule était sous une forte pluie, pour laisser toute humidité de surface s’évaporer.</li>
</ul>
''',
 cta=dict(titre='Des trottinettes conçues pour tous les temps', texte='Découvrez les pneus 10 pouces gonflables et l’étanchéité IPX5 de la gamme Agaru dans notre comparatif complet.',
          boutons=['<a class="btn btn--primary" href="../comparateur.html#securite">Voir les critères de sécurité <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(ULTRA, 'Fiche technique sur augment.eco')]),
 faq=[
  ('Peut-on rouler sous une grosse pluie en trottinette électrique ?', 'Oui, si la trottinette est certifiée au moins IPX5 comme l’Augment Agaru. Elle résiste aux fortes projections d’eau, mais il ne faut jamais plonger le plateau dans des flaques profondes.'),
  ('Pourquoi la trottinette glisse-t-elle sur les bandes blanches quand il pleut ?', 'La peinture routière et la résine des passages piétons perdent toute rugosité une fois mouillées. Il faut impérativement ralentir avant et traverser ces marquages en ligne droite sans freiner.'),
  ('Faut-il nettoyer sa trottinette après avoir roulé sous la pluie ?', 'Il est conseillé de passer un chiffon doux pour sécher le châssis et retirer les projections de boue ou de sel de voirie qui pourraient gripper les roulements à long terme.'),
  ('Peut-on recharger une trottinette mouillée ?', 'Attendez toujours que la prise et le plateau soient totalement secs avant d’insérer l’embout du chargeur 220V, afin d’éviter tout court-circuit.'),
 ],
 sources=[('Comprendre les indices de protection IP : Commission Électrotechnique Internationale (IEC 60529)', 'https://www.iec.ch/ip-ratings'),
          ('Sécurité routière : conseils de conduite pour les engins de déplacement personnel motorisés (EDPM)', 'https://www.securite-routiere.gouv.fr/chacun-son-mode-de-deplacement/dpm-trottinette-electrique'),
          ('Guide d’entretien et étanchéité : help.augment.eco/fr', 'https://help.augment.eco/fr/articles/6462720-etancheite-et-pluie')],
 lies=['batterie-trottinette-electrique-duree-de-vie', 'trottinette-electrique-volee-que-faire', 'trottinette-electrique-ecologique'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='trottinette-ou-scooter-electrique-choisir',
 categorie='Comparatif',
 titre_seo='Trottinette ou scooter électrique : lequel choisir en ville ?',
 description='Trottinette 25 km/h ou cyclomoteur 45 km/h pliable ? Pistes cyclables, voies rapides, permis, rangement et budget : faites le bon choix pour votre quotidien.',
 h1='Trottinette ou scooter électrique pliable&nbsp;: quel véhicule pour votre trajet&nbsp;?',
 chapo='D’un côté, la légèreté de la trottinette électrique qui se faufile sur les pistes cyclables à 25&nbsp;km/h. De l’autre, la puissance d’un cyclomoteur à assise qui roule à 45&nbsp;km/h dans le flux de circulation tout en se pliant pour monter chez vous. Lequel correspond le mieux à votre routine urbaine ?',
 image=('scooter-360-cour', 'Un scooter électrique pliable 360 et une trottinette électrique garés côte à côte dans une cour parisienne'),
 anim=False,
 lecture=7,
 en_bref=[
  'Pour les trajets de moins de 6 km en centre-ville, la trottinette est imbattable grâce au réseau cyclable.',
  'Au-delà de 8 km ou sur des axes périurbains limités à 50 km/h, le scooter 45 km/h fait gagner un temps précieux.',
  'La trottinette monte partout (20 kg) ; le scooter 360 (36 kg) se roule plus qu’il ne se porte et exige un ascenseur.',
  'La trottinette se conduit sans permis dès 14 ans ; le cyclomoteur requiert le permis AM (ou permis B), casque moto et carte grise.',
 ],
 corps='''
<h2 id="infrastructure">Pistes cyclables ou chaussée : où allez-vous rouler&nbsp;?</h2>
<p>C’est la première question à vous poser avant même de regarder les fiches techniques. Les deux véhicules n’ont pas le même statut juridique ni les mêmes droits d’accès à la ville :</p>
<ul class="check">
 <li><strong>L’Agaru (trottinette 25 km/h)</strong> est un EDPM. Elle doit obligatoirement emprunter les <strong>pistes cyclables</strong> dès qu’elles existent. C’est un avantage considérable dans les métropoles saturées (Paris, Lyon, Bordeaux, Nantes) : vous roulez à l’écart des voitures, sans bouchons ni feux rouges interminables.</li>
 <li><strong>L’E-scooter 360 (cyclomoteur 45 km/h)</strong> appartient à la catégorie <strong>L1e</strong>. Il est <strong>interdit sur les pistes cyclables</strong> et sur les trottoirs : vous circulez directement sur la chaussée avec les voitures, bus et motos. À 45 km/h, vous vous insérez sans encombre dans le flot urbain sans vous faire frôler.</li>
</ul>

<h2 id="distance">La distance quotidienne : le seuil des 8 kilomètres</h2>
<p>Sur un trajet de 3 à 5 kilomètres (environ 12 à 15 minutes en trottinette), être debout ne pose aucun problème de confort. La trottinette se plie en 3 secondes et vous suit dans votre bureau ou votre café préféré.</p>
<p>En revanche, dès que votre aller simple atteint <strong>8 à 15 kilomètres</strong>, ou comporte des montées prononcées et des départementales périurbaines, la position assise et la puissance font toute la différence :</p>
<ul class="dash">
 <li>Le moteur de <strong>2 140 W</strong> de l’E-scooter 360 gravit n’importe quelle côte à pleine vitesse sans ralentir.</li>
 <li>La selle rembourrée et les <strong>larges pneus ballons de 10 pouces (120/90-R10)</strong> gomment les nids-de-poule et les pavés là où une trottinette debout transmet les vibrations aux jambes et aux bras.</li>
 <li>Sur 12 kilomètres, rouler à 45 km/h permet de boucler le trajet en 18 minutes contre 35 minutes sur une trottinette bridée à 25 km/h.</li>
</ul>

<h2 id="tableau-comparatif">Le comparatif face à face</h2>
<div class="art-table-wrap">
<table class="art-table">
 <caption>Comparatif Agaru Ultra vs Augment E-scooter 360 (données 2026)</caption>
 <thead><tr><th scope="col">Critère</th><th scope="col">Agaru Ultra</th><th scope="col">E-scooter 360</th></tr></thead>
 <tbody>
  <tr><th scope="row">Catégorie légale</th><td>EDPM (trottinette)</td><td>Cyclomoteur L1e (scooter 50cc)</td></tr>
  <tr><th scope="row">Vitesse maximale</th><td>25 km/h</td><td>45 km/h</td></tr>
  <tr><th scope="row">Voies autorisées</th><td>Pistes cyclables, voies vertes</td><td>Chaussée uniquement (interdit sur pistes)</td></tr>
  <tr><th scope="row">Permis requis</th><td>Aucun (dès 14 ans)</td><td>Permis AM ou Permis B (dispense avant 1988)</td></tr>
  <tr><th scope="row">Plaque &amp; carte grise</th><td>Non</td><td>Oui (immatriculation obligatoire)</td></tr>
  <tr><th scope="row">Équipement obligatoire</th><td>Gilet rétro la nuit (casque conseillé)</td><td>Casque homologué + gants homologués</td></tr>
  <tr><th scope="row">Batterie &amp; autonomie</th><td>768 Wh fixe (55 à 70 km)</td><td>1 080 Wh amovible (53 km / 106 km double)</td></tr>
  <tr><th scope="row">Poids total</th><td>20,7 kg</td><td>36 kg (avec batterie)</td></tr>
  <tr><th scope="row">Rangement plié</th><td>Sous un bureau, coffre, train</td><td>Entrée, ascenseur (126 × 35 × 118 cm)</td></tr>
  <tr><th scope="row">Prix à l’achat</th><td>549 €</td><td>1 990 €</td></tr>
  <tr><th scope="row">Location mensuelle</th><td>Dès 12,95 €/mois (réparations incluses)</td><td>Dès 25,90 €/mois (garantie 2 ans)</td></tr>
 </tbody>
</table>
</div>

<h2 id="logistique-maison">La logistique chez soi : ascenseur, marches et recharge</h2>
<p>C’est souvent le critère décisif qui départage les deux engins :</p>
<p>Avec ses <strong>20,7 kg</strong>, l’Agaru Ultra peut être montée sur un ou deux étages sans ascenseur, même si cela demande un peu d’effort. Elle se glisse sans encombre dans un placard d’entrée ou sous un lit mezzanine.</p>
<p>Avec ses <strong>36 kg</strong>, l’E-scooter 360 ne se porte pas dans des escaliers étroits au quotidien. En revanche, son pliage ultra-compact (sa roue arrière pivote sous la selle) lui permet de rentrer dans les ascenseurs parisiens les plus exigus. Et surtout : <strong>sa batterie de 5,2 kg est amovible</strong>. Vous pouvez laisser le châssis dans un local à vélos ou dans le coffre d’une voiture et ne monter que la batterie chez vous pour la recharger en quelques heures sur une prise secteur ordinaire.</p>
''',
 cta=dict(titre='Simulez votre véhicule idéal', texte='Comparez en direct les mensualités de location de l’Agaru Ultra et de l’E-scooter 360 selon votre durée d’engagement.',
          boutons=['<a class="btn btn--primary" href="../comparateur.html">Voir le comparatif complet <span class="arr" aria-hidden="true">→</span></a>', '<a class="btn btn--secondary" href="../configurateur.html">Accéder au simulateur <span class="arr" aria-hidden="true">→</span></a>']),
 faq=[
  ('Peut-on rouler sur les pistes cyclables avec un scooter électrique 45 km/h ?', 'Non. Tout véhicule homologué dans la catégorie cyclomoteur L1e (capable d’atteindre 45 km/h) a l’obligation de circuler sur la chaussée et n’a pas le droit d’emprunter les pistes ou bandes cyclables.'),
  ('Quel est le principal avantage de l’E-scooter 360 par rapport à un scooter classique ?', 'Son châssis pliable breveté et sa batterie amovible : vous pouvez le ranger directement dans votre appartement ou au bureau sans avoir besoin d’un garage fermé ni d’une borne de recharge dans la rue.'),
  ('La trottinette électrique est-elle plus rapide qu’un scooter en centre-ville ?', 'Sur des distances courtes (moins de 5 km) aux heures de pointe, la trottinette est souvent plus rapide car elle utilise les couloirs cyclables continus et évite les embouteillages de voitures.'),
  ('Peut-on transporter un passager sur un scooter électrique pliable ?', 'L’E-scooter 360 est un véhicule monoplace homologué pour une seule personne (charge utile maximale de 100 kg), tout comme les trottinettes électriques.'),
 ],
 sources=[('Réglementation des cyclomoteurs L1e : Service-Public.fr', 'https://www.service-public.fr/particuliers/vosdroits/F31825'),
          ('Code de la route : circulation des engins de déplacement personnel motorisés (EDPM)', 'https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074228/LEGISCTA000039270503/'),
          ('Fiches comparatives officielles : augment.eco/fr-fr', 'https://augment.eco/fr-fr/')],
 lies=['scooter-electrique-pliable-45-km-h', 'agaru-smart-ou-agaru-ultra-difference', 'trottinette-electrique-ecologique'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='batterie-trottinette-electrique-duree-de-vie',
 categorie='Technique',
 titre_seo='Batterie trottinette électrique : durée de vie et entretien',
 description='Combien de temps dure la batterie d’une trottinette ? L’impact méconnu du froid hivernal, la règle 20-80 % et le coût réel d’un remplacement.',
 h1='Batterie de trottinette électrique&nbsp;: longévité, pièges de l’hiver et bonnes pratiques',
 chapo='C’est le cœur de votre engin et l’élément le plus cher à remplacer : la batterie représente près de la moitié de la valeur d’une trottinette électrique. Combien d’années peut-elle réellement tenir ? Pourquoi votre autonomie fond-elle en hiver ? Voici tout ce que vous devez savoir pour la préserver au maximum.',
 image=('guide-frein-arriere', 'Détail du châssis en aluminium protégeant le bloc batterie intégré sous le plateau'),
 anim=False,
 lecture=6,
 en_bref=[
  'Une batterie Li-ion de qualité supporte entre 500 et 800 cycles complets, soit 15 000 à 25 000 kilomètres de trajet.',
  'En dessous de 5 °C, les réactions chimiques ralentissent : vous perdez naturellement 20 à 30 % d’autonomie.',
  'Ne chargez jamais une batterie encore glacée : laissez-la toujours revenir à température ambiante avant de brancher le câble.',
  'Pour maximiser la longévité, maintenez la charge entre 20 % et 80 % au quotidien lors de vos trajets de semaine.',
 ],
 corps='''
<h2 id="duree-vie-cycles">Combien de temps dure une batterie de trottinette&nbsp;?</h2>
<p>Sur les modèles récents comme l’Agaru Smart (499 Wh) ou l’Agaru Ultra (768 Wh), le constructeur utilise des cellules lithium-ion cylindriques de type <strong>21700</strong> de haute densité énergétique. Ces accumulateurs sont donnés pour <strong>500 à 800 cycles de charge complets</strong> avant que leur capacité ne descende en dessous de 80 % de son niveau d’origine.</p>
<p>Concrètement, sur une Agaru Ultra qui offre environ 50 à 60 kilomètres d’autonomie réelle par charge :</p>
<ul class="check">
 <li>500 cycles représentent environ <strong>25 000 kilomètres</strong> au compteur.</li>
 <li>Pour un utilisateur urbain moyen parcourant 10 kilomètres par jour ouvré (environ 2 200 km par an), la batterie conserve d’excellentes performances pendant <strong>plus de 5 à 7 ans</strong>.</li>
</ul>
<p>Ce qui tue prématurément une batterie, ce ne sont pas les kilomètres parcourus, mais les erreurs d’usage : la décharge profonde prolongée et les écarts thermiques extrêmes.</p>

<h2 id="hiver-froid">Pourquoi l’autonomie s’effondre en hiver&nbsp;?</h2>
<p>Dès que le thermomètre passe sous la barre des 5 °C, vous constatez que votre jauge de batterie descend plus vite que d’habitude. Ce n’est pas une panne : c’est une propriété physique du lithium.</p>
<p>Le froid augmente la résistance interne de l’électrolyte liquide au sein des cellules. Les ions lithium se déplacent moins vite, la tension chute plus vite sous l’effort du moteur et la batterie délivre moins d’énergie utile. Vous perdez couramment <strong>20 à 30 % d’autonomie réelle</strong> à 0 °C par rapport à un trajet effectué par 20 °C.</p>
<aside class="tip"><p class="tip__t">La règle d’or de la recharge en hiver</p><p>Ne branchez <strong>JAMAIS</strong> votre trottinette en charge immédiatement après avoir roulé dans le froid si elle est restée dehors. Recharger des cellules lithium à une température inférieure à 0 °C provoque un phénomène irréversible de placage métallique (dépôt de lithium pur sur l’anode) qui détruit la capacité de la batterie et peut causer un court-circuit interne. Laissez-la toujours se réchauffer 1 heure à température ambiante dans votre logement avant de lancer la charge.</p></aside>

<h2 id="regle-20-80">La règle des 20 % - 80 % pour doubler sa durée de vie</h2>
<p>Les batteries lithium-ion n’ont plus d’effet mémoire (inutile de les vider complètement avant de recharger, c’est même déconseillé). En revanche, elles subissent une forte tension mécanique lorsqu’elles sont pleines à 100 % ou vides à 0 %.</p>
<ul class="dash">
 <li><strong>Au quotidien :</strong> si votre trajet ne demande que 15 ou 20 km, vous n’avez pas besoin d’atteindre 100 % à chaque fois. Débrancher vers 80 % ou 90 % divise par trois la dégradation chimique des cellules.</li>
 <li><strong>Ne laissez pas la trottinette à plat :</strong> si la jauge passe sous 10 %, rechargez dès votre arrivée. Laisser une trottinette déchargée à 0 % pendant plusieurs semaines dans une cave fait tomber les cellules en sous-tension critique : le circuit de sécurité (BMS) bloque alors définitivement la batterie.</li>
 <li><strong>Stockage prolongé :</strong> si vous n’utilisez pas votre trottinette pendant les vacances d’été ou d’hiver, stockez-la avec un niveau de charge d’environ <strong>50 à 60 %</strong>, dans un endroit tempéré et sec (entre 15 °C et 25 °C).</li>
</ul>

<h2 id="remplacement-prix">Combien coûte un changement de batterie&nbsp;?</h2>
<p>Si vous possédez votre trottinette, le remplacement d’un pack complet de 768 Wh hors garantie coûte entre <strong>250 et 350 €</strong>, pièces et main-d’œuvre comprises. C’est souvent à ce moment-là que beaucoup d’acheteurs hésitent à jeter leur engin.</p>
<p>C’est l’un des atouts centraux de la formule d’abonnement Augment : la batterie fait partie des <strong>composants couverts par le service de réparation</strong>. Si la capacité de votre Agaru Ultra chute de façon anormale ou tombe en panne, le remplacement du bloc ou de la trottinette est entièrement pris en charge sans surcoût.</p>
''',
 cta=dict(titre='Ne craignez plus la panne de batterie', texte='Avec le service tout compris d’Augment, l’usure de la batterie et les réparations sont incluses pendant toute la durée de votre location.',
          boutons=['<a class="btn btn--primary" href="../comparateur.html#service">Découvrir le service Augment <span class="arr" aria-hidden="true">→</span></a>', lien_partenaire(ULTRA, 'Voir l’Agaru Ultra sur augment.eco')]),
 faq=[
  ('Peut-on laisser sa trottinette électrique branchée toute la nuit ?', 'Oui, les chargeurs modernes et le boîtier de gestion électronique (BMS) coupent automatiquement le courant une fois la charge complète atteinte. Il reste néanmoins conseillé de débrancher dès que le voyant passe au vert pour éviter les micros-cycles d’entretien.'),
  ('Pourquoi la trottinette avance-t-elle moins vite quand la batterie est faible ?', 'La tension globale du pack diminue au fur et à mesure de la décharge. Le contrôleur réduit la puissance envoyée au moteur pour protéger les cellules contre la sous-tension.'),
  ('Est-il possible d’augmenter la capacité de batterie de son Agaru Smart ?', 'Les châssis de l’Agaru Smart (499 Wh) et de l’Agaru Ultra (768 Wh) sont identiques, mais le pack batterie et le contrôleur sont calibrés en usine. Il n’est pas recommandé de modifier la batterie soi-même sous peine d’annuler les garanties et certifications.'),
  ('Que faire de son ancienne batterie de trottinette ?', 'Les batteries lithium sont des déchets dangereux recyclables à plus de 70 %. Déposez-les gratuitement dans un point de collecte officiel Corepile ou Screlec, en déchetterie ou auprès de votre réparateur.'),
 ],
 sources=[('Filière de recyclage des accumulateurs et batteries : Corepile France', 'https://www.corepile.fr/'),
          ('Batteries lithium-ion : conseils de sécurité et risques thermiques : INRS', 'https://www.inrs.fr/risques/incendie-explosion/batteries-lithium.html'),
          ('Données techniques batteries Augment : augment.eco/fr-fr/agaru-ultra', 'https://augment.eco/fr-fr/agaru-ultra/')],
 lies=['rouler-sous-la-pluie-trottinette-electrique', 'agaru-smart-ou-agaru-ultra-difference', 'trottinette-electrique-ecologique'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='agaru-smart-ou-agaru-ultra-difference',
 categorie='Gamme',
 titre_seo='Agaru Smart ou Agaru Ultra : quelles différences ?',
 description='Même moteur 500W, même châssis, mais 150 € d’écart : batterie 499 Wh vs 768 Wh, autonomie réelle et formules de location. Quel modèle choisir ?',
 h1='Agaru Smart ou Agaru Ultra&nbsp;: les 768&nbsp;Wh valent-ils l’écart de prix&nbsp;?',
 chapo='Au premier coup d’œil, impossible de les distinguer : elles partagent exactement le même design noir mat, les mêmes roues de 10 pouces et le même moteur de 500 W. Pourtant, l’une coûte 399 € et l’autre 549 €, et seule l’Ultra est proposée en location. Voici le comparatif détaillé pour faire le bon choix.',
 image=('guide-agaru-pneu', 'Détail de la roue avant et de la potence épurée de la gamme trottinette électrique Augment Agaru'),
 anim=False,
 lecture=5,
 en_bref=[
  'Les deux modèles partagent le même moteur (500 W nominal / 800 W crête, 26 Nm, pentes jusqu’à 23 %).',
  'Même confort et sécurité : pneus gonflables 10 pouces, frein à disque arrière mécanique et eABS avant.',
  'La seule vraie différence mécanique : la batterie (499 Wh sur la Smart vs 768 Wh sur l’Ultra).',
  'L’Agaru Smart s’achète uniquement comptant (ou crédit PayPal) ; l’Agaru Ultra est la seule proposée en abonnement mensuel.',
 ],
 corps='''
<h2 id="points-communs">Ce qui est rigoureusement identique</h2>
<p>Augment a fait le choix d’une plateforme industrielle unique. Que vous choisissiez la Smart ou l’Ultra, vous bénéficiez exactement des mêmes caractéristiques de châssis et de sécurité :</p>
<ul class="check">
 <li><strong>Moteur et couple :</strong> moteur brushless logé dans la roue avant développant <strong>500 W nominaux et 800 W en puissance de crête</strong> avec un couple généreux de 26 Nm, capable de gravir des pentes jusqu’à 23 %.</li>
 <li><strong>Freinage :</strong> étrier à disque mécanique sur la roue arrière combiné à un frein moteur régénératif électronique (eABS) à l’avant pour un arrêt sécurisant en toute circonstance.</li>
 <li><strong>Roues et confort :</strong> pneus de 10 × 2,5 pouces avec chambre à air pour absorber les déformations de la chaussée.</li>
 <li><strong>Équipement urbain :</strong> écran LED central, phare avant, feu stop arrière et clignotants intégrés aux extrémités du guidon.</li>
 <li><strong>Étanchéité :</strong> certification IPX5 pour rouler sous la pluie sans inquiétude.</li>
</ul>

<h2 id="differences-cles">Ce qui change : capacité, autonomie et poids</h2>
<p>L’écart se joue entièrement sous le tapis en silicone du plateau, à l’intérieur du boîtier aluminium étanche :</p>
<div class="art-table-wrap">
<table class="art-table">
 <caption>Différences techniques directes Agaru Smart vs Agaru Ultra</caption>
 <thead><tr><th scope="col">Caractéristique</th><th scope="col">Agaru Smart</th><th scope="col">Agaru Ultra</th></tr></thead>
 <tbody>
  <tr><th scope="row">Capacité batterie</th><td>499 Wh (36 V / 13,8 Ah)</td><td><strong>768 Wh</strong> (36 V / 21,3 Ah)</td></tr>
  <tr><th scope="row">Autonomie constructeur</th><td>Jusqu’à 50 km</td><td><strong>Jusqu’à 70 km</strong></td></tr>
  <tr><th scope="row">Autonomie réelle constatée</th><td>30 à 40 km (selon poids et dénivelé)</td><td><strong>50 à 60 km</strong> (grand rayon d’action)</td></tr>
  <tr><th scope="row">Poids du véhicule</th><td>20,0 kg</td><td>20,7 kg (+700 g pour les cellules en plus)</td></tr>
  <tr><th scope="row">Temps de charge 0-100 %</th><td>Environ 5 h</td><td>Environ 7 h 30</td></tr>
  <tr><th scope="row">Prix d’achat comptant</th><td><strong>399 €</strong></td><td>549 € (+150 €)</td></tr>
  <tr><th scope="row">Disponibilité en abonnement</th><td>Non disponible</td><td><strong>Dès 12,95 €/mois</strong> (réparations incluses)</td></tr>
 </tbody>
</table>
</div>

<h2 id="pour-qui-smart">Pourquoi choisir l’Agaru Smart à 399&nbsp;€&nbsp;?</h2>
<p>L’Agaru Smart est l’un des meilleurs rapports qualité/prix du marché pour un achat direct :</p>
<ul class="dash">
 <li>Vous parcourez <strong>moins de 10 à 15 km par jour</strong> (trajet domicile-travail classique de 5 à 7 km aller-retour).</li>
 <li>Vous pouvez recharger votre trottinette tous les deux ou trois jours sans stress.</li>
 <li>Vous voulez acheter votre engin au comptant sans mensualité ni engagement : à 399 €, elle est moins chère que la plupart des trottinettes chinoises de puissance équivalente tout en offrant des pneus 10" et un frein à disque.</li>
</ul>

<h2 id="pour-qui-ultra">Pourquoi investir dans l’Agaru Ultra à 549&nbsp;€ (ou en location)&nbsp;?</h2>
<p>Les 269 Wh supplémentaires (+54 % de batterie) apportent un confort d’usage radical au quotidien :</p>
<ul class="check">
 <li><strong>Moins de recharges :</strong> avec 55 km réels, un utilisateur urbain moyen ne la branche qu’une seule fois par semaine.</li>
 <li><strong>Maintien de la puissance :</strong> une batterie de 768 Wh maintient une tension élevée plus longtemps. Dans les côtes à 15 %, l’Ultra conserve ses 25 km/h même lorsque la jauge passe sous 50 %, là où une batterie plus petite commence à brider sa puissance.</li>
 <li><strong>L’accès à l’abonnement Augment :</strong> c’est le modèle vedette de la formule tout compris. Dès 12,95 €/mois, vous bénéficiez de l’assistance, des pièces d’usure et du remplacement gratuit en cas de panne, ce qui n’existe pas sur la Smart.</li>
</ul>
''',
 cta=dict(titre='Quel modèle correspond à votre budget&nbsp;?', texte='Simulez votre achat ou votre location et calculez vos économies mensuelles sur l’Agaru Ultra dans notre outil interactif.',
          boutons=['<a class="btn btn--primary" href="../configurateur.html">Configurer mon Agaru <span class="arr" aria-hidden="true">→</span></a>', '<a class="btn btn--secondary" href="../comparateur.html#gamme">Comparer les 14 critères <span class="arr" aria-hidden="true">→</span></a>']),
 faq=[
  ('L’Agaru Ultra est-elle plus rapide que l’Agaru Smart ?', 'Non. Les deux modèles sont légalement bridés à 25 km/h conformément au Code de la route pour les engins de déplacement personnel motorisés. En revanche, l’Ultra maintient sa vitesse maximale plus facilement dans les montées lorsque la batterie faiblit.'),
  ('Peut-on louer l’Agaru Smart ?', 'Non, sur le marché français, Augment ne propose la formule d’abonnement avec réparations incluses que sur l’Agaru Ultra et l’E-scooter 360. L’Agaru Smart est réservée à l’achat comptant ou au paiement échelonné.'),
  ('Les pièces détachées sont-elles interchangeables entre la Smart et l’Ultra ?', 'Oui, à l’exception du pack batterie interne, toutes les pièces (pneus, chambres à air, leviers, plaquettes de frein, écran, potence et garde-boue) sont strictement identiques.'),
  ('L’Agaru Ultra est-elle beaucoup plus lourde ?', 'La différence n’est que de 700 grammes (20,7 kg contre 20,0 kg), ce qui correspond uniquement au poids des cellules lithium supplémentaires à l’intérieur du plateau.'),
 ],
 sources=[('Fiche produit Agaru Smart : augment.eco/fr-fr/agaru-smart', 'https://augment.eco/fr-fr/agaru-smart/'),
          ('Fiche produit Agaru Ultra : augment.eco/fr-fr/agaru-ultra', 'https://augment.eco/fr-fr/agaru-ultra/'),
          ('Relevé des tarifs et grilles de financement : configurateur Augment officiel', 'https://augment.eco/fr-fr/')],
 lies=['batterie-trottinette-electrique-duree-de-vie', 'louer-ou-acheter-trottinette-electrique', 'trottinette-ou-scooter-electrique-choisir'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='prendre-le-train-avec-sa-trottinette-electrique',
 categorie='Pratique',
 titre_seo='Trottinette électrique dans le train : règles SNCF et TER',
 description='TGV, TER, Ouigo, Transilien ou métro : règles officielles, dimensions maximales admises, rangement à bord et recharge interdite. Le guide complet.',
 h1='Prendre le train avec sa trottinette électrique&nbsp;: le guide des règles SNCF et TER',
 chapo='Combiner le train et la trottinette électrique est la solution parfaite pour les trajets domicile-travail interurbains. Mais attention aux mauvaises surprises sur le quai : les contrôleurs appliquent désormais des consignes strictes sur le pliage, le gabarit et l’emplacement à bord. Voici le point complet pour voyager sans stress ni amende.',
 image=('ecologie-trottinette-tram', 'Une trottinette électrique pliée posée au sol à côté d’un quai de gare en attendant l’embarquement'),
 anim=False,
 lecture=5,
 en_bref=[
  'À bord des TGV InOui, TER et Ouigo, votre trottinette voyage gratuitement si elle est pliée et mesure moins de 130 × 90 cm.',
  'Elle doit obligatoirement être pliée dès l’accès aux quais et pendant toute la durée du trajet.',
  'Rangez-la dans les racks à bagages bas situés à l’entrée des voitures, jamais dans le couloir central.',
  'Il est formellement interdit de recharger sa trottinette sur les prises 220V à bord des trains.',
 ],
 corps='''
<h2 id="regles-sncf">Les règles officielles à la SNCF (TGV, Ouigo et TER)</h2>
<p>La SNCF assimile la trottinette électrique pliée à un <strong>bagage à main ordinaire</strong>. À ce titre, son transport est entièrement gratuit et ne nécessite aucun billet supplémentaire ni réservation de place vélo.</p>
<p>Vous devez toutefois respecter trois critères impératifs :</p>
<ol>
 <li><strong>Le pliage obligatoire :</strong> vous devez plier la potence avant de franchir les portiques d’accès ou de descendre sur le quai. Rouler sur le quai ou dans les couloirs de gare est passible d’une amende forfaitaire de 150 €.</li>
 <li><strong>Les dimensions maximales :</strong> le bagage ne doit pas dépasser <strong>130 × 90 cm</strong> une fois replié. L’Agaru d’Augment affiche 118 × 48 cm repliée : elle rentre largement dans les clous réglementaires.</li>
 <li><strong>L’étiquetage visible :</strong> comme pour n’importe quelle valise, une étiquette avec votre nom, prénom et numéro de téléphone doit être attachée au guidon ou au cadre.</li>
</ol>

<h2 id="ou-la-ranger">Où la ranger dans la rame&nbsp;?</h2>
<p>C’est le point de friction le plus fréquent avec les chefs de bord. La règle de sécurité ferroviaire est intransigeante : <strong>aucun bagage ne doit entraver les voies de circulation</strong> ou l’accès aux issues de secours.</p>
<ul class="check">
 <li><strong>L’emplacement idéal :</strong> les racks à bagages horizontaux situés à l’entrée des voitures. Placez la trottinette sur l’étagère du bas, plateau vers le fond et guidon vers l’avant pour éviter qu’elle ne glisse au freinage.</li>
 <li><strong>L’espace entre deux sièges dos à dos :</strong> dans beaucoup de TGV et de rames TER, l’espace triangulaire formé par deux dossiers dos à dos accueille parfaitement une trottinette pliée posée sur la tranche.</li>
 <li><strong>Ce qui est strictement interdit :</strong> laisser la trottinette dans le couloir central entre les sièges, la poser sur la plateforme d’entrée devant les portes d’évacuation ou la monter sur les porte-bagages suspendus au-dessus de la tête des voyageurs (risque mortel en cas de freinage d’urgence).</li>
</ul>

<h2 id="metro-rer-transilien">Qu’en est-il dans le métro, le RER et le tramway&nbsp;?</h2>
<p>En Île-de-France (réseau RATP et Île-de-France Mobilités) ainsi que dans les réseaux de transport urbain des grandes métropoles (TBM à Bordeaux, TCL à Lyon, RTM à Marseille) :</p>
<ul class="dash">
 <li>La trottinette pliée tenue à la main est acceptée <strong>à toute heure</strong> sans supplément.</li>
 <li>La trottinette dépliée est formellement interdite à bord des bus, tramways et rames de métro.</li>
 <li>Aux heures de pointe (7h30-9h30 et 16h30-19h00), tenez la trottinette verticalement posée sur sa roue avant entre vos jambes pour limiter l’encombrement au sol et ne pas salir les passagers voisins.</li>
</ul>

<h2 id="recharge-train">Peut-on recharger sa trottinette dans le train&nbsp;?</h2>
<p>La réponse est un <strong>NON catégorique</strong>. Les prises électriques 220V mises à disposition des voyageurs en 1<sup>re</sup> ou 2<sup>nde</sup> classe dans les TGV sont calibrées pour des appareils à faible puissance (ordinateurs portables, smartphones, rasoirs, puissance maximale autorisée de 100 à 150 W).</p>
<p>Le chargeur d’une trottinette électrique demande entre 120 W et 250 W avec un appel de courant important à l’allumage. Brancher votre chargeur de trottinette déclenche les disjoncteurs différentiels de la rame et expose à une verbalisation immédiate par les agents du train.</p>
<aside class="tip"><p class="tip__t">Le conseil multimodal Roulelibre</p><p>Avec ses 20,7 kg, porter une Agaru Ultra dans les escaliers des gares sans escalator devient vite fatigant. L’astuce : laissez le crochet de potence engagé dans le garde-boue arrière, tenez la potence d’une main et faites rouler l’engin sur sa seule roue avant comme un chariot à roulettes. Vous ne portez ainsi qu’un tiers du poids réel.</p></aside>
''',
 cta=dict(titre='Facilitez vos trajets du quotidien', texte='Découvrez comment la trottinette électrique pliable remplace avantageusement la voiture en complément des transports en commun.',
          boutons=['<a class="btn btn--primary" href="forfait-mobilites-durables-trottinette-electrique.html">Voir le forfait mobilités durables <span class="arr" aria-hidden="true">→</span></a>', '<a class="btn btn--secondary" href="../comparateur.html">Voir le comparatif complet <span class="arr" aria-hidden="true">→</span></a>']),
 faq=[
  ('Faut-il payer un billet supplémentaire pour une trottinette dans le TGV ?', 'Non. Contrairement aux vélos non démontés qui nécessitent un billet spécifique à 10 €, une trottinette électrique pliée voyage gratuitement en tant que bagage à main ordinaire.'),
  ('Une housse de transport est-elle obligatoire dans le train ?', 'Elle n’est pas obligatoire à bord des trains SNCF ordinaires tant que la trottinette est pliée et propre. Elle reste toutefois vivement recommandée lors des fortes affluences pour éviter les remarques et protéger le cadre.'),
  ('Peut-on emporter un scooter électrique pliable comme l’E-scooter 360 dans le train ?', 'L’E-scooter 360 plié mesure 126,5 cm de long et pèse 36 kg. Il entre tout juste dans le gabarit bagage de 130 cm, mais son poids important le rend très difficile à manipuler sur les quais. En pratique, la SNCF tolère les cyclomoteurs pliants dans les rames TER peu bondées avec espace vélos, mais peut refuser l’accès en TGV si le chef de bord estime que le poids nuit à la sécurité.'),
  ('Que risque-t-on si l’on roule en trottinette dans une gare ?', 'Circuler sur un engin à moteur dans l’enceinte d’une gare ou sur les quais est passible d’une amende de 150 € pour mise en danger de la sécurité des voyageurs.'),
 ],
 sources=[('Règles relatives aux bagages à bord des trains TGV et TER : SNCF Voyageurs', 'https://www.sncf-voyageurs.com/fr/voyagez-avec-nous/en-france/tgv-inoui/services-a-bord/bagages/'),
          ('Règlement général des transports d’Île-de-France Mobilités / RATP', 'https://www.ratp.fr/regles-d-usage-et-de-securite'),
          ('Dimensions et pliage de l’Agaru : augment.eco/fr-fr/agaru-ultra', 'https://augment.eco/fr-fr/agaru-ultra/')],
 lies=['trottinette-electrique-volee-que-faire', 'forfait-mobilites-durables-trottinette-electrique', 'trottinette-electrique-assurance-reglementation'],
),

]
