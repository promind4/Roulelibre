"""Crée a-propos.html (qui sommes-nous, méthode, financement) à partir du gabarit des mentions légales."""
import io, re, glob

S = 'D:/AUGMENT ECO/site/'
src = io.open(S + 'mentions-legales.html', encoding='utf-8').read()

head_title = 'Qui sommes-nous : notre méthode et nos sources'
head_desc = 'Qui édite ce site, comment nous relevons les prix et les caractéristiques des trottinettes Augment, d’où viennent les avis, et comment le site est financé.'

body = '''<main id="contenu">
  <div class="wrap legal">
    <header class="legal__head">
      <span class="eyebrow">Qui sommes-nous</span>
      <h1 id="titre-page">Notre méthode, nos sources.</h1>
      <p class="lead">Ce site aide à choisir entre l’Agaru Smart, l’Agaru Ultra et l’E-scooter 360, et entre la location et l’achat. Voici qui l’écrit, d’où viennent les chiffres et ce que nous ne faisons pas.</p>
    </header>
    <div class="legal__grid">
      <nav class="legal__toc" aria-label="Sommaire">
        <span class="label">Sommaire</span>
        <a href="#qui">Qui édite le site</a>
        <a href="#pourquoi">Pourquoi ce site</a>
        <a href="#methode">Comment nous travaillons</a>
        <a href="#avis">Avis et vidéos</a>
        <a href="#limites">Ce que nous ne faisons pas</a>
        <a href="#financement">Comment le site est financé</a>
        <a href="#corrections">Signaler une erreur</a>
      </nav>
      <div class="prose">
        <section aria-labelledby="qui">
          <h2 id="qui">Qui édite le site</h2>
          <p>Le site est édité par Kesiah Ntumba, entrepreneur individuel installé à Bordeaux (nom commercial Azura). Il relit chaque article avant sa publication et à chaque mise à jour. Coordonnées complètes dans les <a href="/mentions-legales">mentions légales</a>&nbsp;; pour nous écrire&nbsp;: <a href="mailto:contact@roulelibre.fr">contact@roulelibre.fr</a>. Nous ne sommes ni Augment ni un revendeur&nbsp;: aucun véhicule n’est vendu ici, la commande se fait toujours sur augment.eco.</p>
        </section>

        <section aria-labelledby="pourquoi">
          <h2 id="pourquoi">Pourquoi ce site</h2>
          <p>Sur le site d’Augment, les informations utiles pour choisir sont réparties entre les fiches produits, le tunnel de commande, la FAQ et le centre d’aide. Les mensualités changent selon la durée et l’acompte, et la location n’existe pas pour tous les modèles. Nous réunissons ces éléments sur une seule page, avec un simulateur qui reprend la grille réelle, pour répondre à deux questions&nbsp;: quel modèle, et faut-il louer ou acheter.</p>
        </section>

        <section aria-labelledby="methode">
          <h2 id="methode">Comment nous travaillons</h2>
          <ul>
            <li><strong>Les prix</strong> sont relevés dans le tunnel de commande d’augment.eco (édition France), modèle par modèle, pour chaque durée (12, 24, 36&nbsp;mois) et chaque palier d’acompte. Nous ne reprenons pas les prix des pages promotionnelles ou des balises cachées, qui peuvent être anciens.</li>
            <li><strong>Les caractéristiques</strong> (autonomie, vitesse, poids, batterie, freins, dimensions) viennent du panneau «&nbsp;Voir les spécifications&nbsp;» d’augment.eco, des manuels et du centre d’aide help.augment.eco.</li>
            <li><strong>Les conditions</strong> (essai de 14&nbsp;jours, option d’achat, service de réparation, couverture vol) sont reprises de la FAQ et des fiches d’Augment, et attribuées comme telles.</li>
            <li><strong>Les règles de circulation et d’assurance</strong> renvoient aux sources officielles (Code de la route, service-public.fr) plutôt qu’à des résumés.</li>
            <li><strong>Les mises à jour</strong>&nbsp;: les prix et les offres d’Augment changent. Nous les revérifions régulièrement et un relevé automatique est en cours de mise en place pour repérer chaque modification. En cas d’écart, le prix affiché sur augment.eco au moment de la commande fait foi.</li>
          </ul>
        </section>

        <section aria-labelledby="avis">
          <h2 id="avis">Avis et vidéos</h2>
          <p>Les notes viennent de Trustpilot (avis sur Augment, tous pays) et de Google Play (application Augment). Les extraits sont courts, cités tels quels, avec le prénom et l’initiale, le pays et la date. Nous affichons aussi la répartition des notes, avis négatifs compris&nbsp;: ne montrer que les meilleurs serait trompeur.</p>
          <p>Les vidéos sont des essais publiés par des médias et des chaînes indépendantes. Les vidéos de la chaîne d’Augment et celle de son partenaire Ajo Motorsport sont signalées comme telles.</p>
        </section>

        <section aria-labelledby="limites">
          <h2 id="limites">Ce que nous ne faisons pas</h2>
          <ul>
            <li>Nous n’avons pas encore testé nous-mêmes chaque modèle sur la durée. Quand un article s’appuie sur un essai personnel, il le dit clairement&nbsp;; sinon, il s’appuie sur les sources ci-dessus.</li>
            <li>Nous ne publions pas d’avis inventés ni de notes «&nbsp;maison&nbsp;».</li>
            <li>Nous signalons les limites, même quand elles ne vont pas dans le sens de la vente&nbsp;: sur toute la durée du contrat, la location revient plus cher que l’achat comptant&nbsp;; l’E-scooter 360 n’a pas le service de réparation tout compris des Agaru&nbsp;; l’Agaru Smart ne se loue pas en France.</li>
          </ul>
        </section>

        <section aria-labelledby="financement">
          <h2 id="financement">Comment le site est financé</h2>
          <p>Les boutons vers augment.eco sont des liens partenaires (programme d’affiliation AWIN). Si vous commandez après avoir cliqué, Augment nous verse une commission. Cela ne change rien au prix que vous payez, et cela ne modifie ni nos chiffres ni nos comparaisons.</p>
        </section>

        <section aria-labelledby="corrections">
          <h2 id="corrections">Signaler une erreur</h2>
          <p>Un prix qui a changé, une caractéristique inexacte&nbsp;? Écrivez-nous à <a href="mailto:contact@roulelibre.fr">contact@roulelibre.fr</a>&nbsp;: nous corrigeons et nous mettons la page à jour.</p>
        </section>
      </div>
    </div>
  </div>
</main>'''

s = re.sub(r'<main id="contenu">.*?</main>', lambda m: body, src, count=1, flags=re.S)
s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % head_title, s, count=1, flags=re.S)
s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % head_desc, s, count=1)
s = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">', s, count=1)
s = re.sub(r'\n?<!-- SEO:START -->.*?<!-- SEO:END -->', '', s, flags=re.S)
s = s.replace('aria-current="page"', '')
io.open(S + 'a-propos.html', 'w', encoding='utf-8', newline='').write(s)

# lien dans le pied de page de toutes les pages
for f in glob.glob(S + '*.html') + glob.glob(S + 'tools/partials/*.html'):
    t = io.open(f, encoding='utf-8').read()
    if 'href="/a-propos"' not in t and '<li><a href="/mentions-legales">Mentions légales</a></li>' in t:
        t = t.replace('<li><a href="/mentions-legales">Mentions légales</a></li>',
                      '<li><a href="/a-propos">Qui sommes-nous</a></li>\n        <li><a href="/mentions-legales">Mentions légales</a></li>', 1)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
print('ok')
