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
 description='Votre employeur peut prendre en charge jusqu’à 600 € par an de vos trajets en trottinette électrique, personnelle ou louée. Qui y a droit et comment le demander.',
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
 lies=['louer-ou-acheter-trottinette-electrique', 'scooter-electrique-pliable-45-km-h', 'trottinette-electrique-ecologique'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='louer-ou-acheter-trottinette-electrique',
 categorie='Location',
 titre_seo='Louer ou acheter une trottinette électrique : que choisir ?',
 description='Location longue durée, achat comptant ou paiement en plusieurs fois : on compare le vrai coût d’une trottinette électrique sur 12, 24 et 36 mois, chiffres à l’appui.',
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
 lies=['forfait-mobilites-durables-trottinette-electrique', 'trottinette-electrique-assurance-reglementation', 'scooter-electrique-pliable-45-km-h'],
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
 lies=['louer-ou-acheter-trottinette-electrique', 'scooter-electrique-pliable-45-km-h', 'trottinette-electrique-ecologique'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='trottinette-electrique-ecologique',
 categorie='Écologie',
 titre_seo='La trottinette électrique est-elle vraiment écologique ?',
 description='Bilan carbone, fabrication, batterie, durée de vie : on fait le point honnêtement sur l’impact d’une trottinette électrique, et sur ce qui la rend vraiment plus verte.',
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
 lies=['louer-ou-acheter-trottinette-electrique', 'trottinette-electrique-assurance-reglementation', 'scooter-electrique-pliable-45-km-h'],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug='scooter-electrique-pliable-45-km-h',
 categorie='Scooter 45 km/h',
 titre_seo='Scooter électrique pliable 45 km/h : permis, assurance, rangement',
 description='Permis AM, carte grise, assurance, casque et gants, rangement en appartement : le guide simple du scooter électrique pliable 45 km/h, avec l’exemple de l’E-scooter 360.',
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
 lies=['louer-ou-acheter-trottinette-electrique', 'trottinette-electrique-assurance-reglementation', 'trottinette-electrique-ecologique'],
),
]
