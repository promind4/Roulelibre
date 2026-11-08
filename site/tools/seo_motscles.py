"""Intégration des mots-clés stratégiques (recherche du 08/11/2026, suggestions Google France).
Voir D:\\AUGMENT ECO\\MOTS_CLES.md pour la carte complète."""
import io, re, sys

S = 'D:/AUGMENT ECO/site/'

def edit(f, reps):
    p = S + f
    s = io.open(p, encoding='utf-8').read()
    for a, b in reps:
        if a not in s:
            sys.exit('introuvable dans %s : %s' % (f, a[:70]))
        s = s.replace(a, b, 1)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)

def meta(f, title, desc):
    p = S + f
    s = io.open(p, encoding='utf-8').read()
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % desc, s, count=1)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)

meta('index.html', 'Location trottinette électrique longue durée : Augment Agaru',
     'Abonnement trottinette électrique ou scooter pliable Augment : Agaru Ultra dès 12,95 €/mois, réparations comprises, livrée chez vous. Location, achat ou LOA : comparez.')
meta('comparateur.html', 'Comparatif trottinette électrique Augment : Agaru et 360',
     'Agaru Smart, Agaru Ultra ou E-scooter 360 : avis, autonomie (50 à 106 km), vitesse, poids, prix à l’achat et en location. Le comparatif complet critère par critère.')
meta('configurateur.html', 'Prix location trottinette électrique : simulateur Augment',
     'Combien coûte une trottinette électrique en location ? Simulez abonnement, LOA ou paiement en plusieurs fois : Agaru Ultra dès 12,95 €/mois, E-scooter 360 dès 25,90 €/mois.')
meta('videos.html', 'Agaru Ultra et Augment 360 : tests et avis en vidéo',
     'Test de l’Agaru Ultra et de l’Augment 360 en vidéo : essais de médias et de chaînes spécialisées, avis, autonomie et prise en main du scooter électrique pliable.')

edit('index.html', [
    ('<h2 id="location-title">Louer plutôt qu’acheter&nbsp;: le cœur du modèle Augment.</h2>',
     '<h2 id="location-title">Location longue durée&nbsp;: louer sa trottinette électrique plutôt que l’acheter.</h2>'),
    ('<h2 id="avis-title">Ils roulent en Augment.</h2>', '<h2 id="avis-title">Avis Augment&nbsp;: ils roulent en Agaru et en 360.</h2>'),
    ('<h2 id="gamme-title">Trois véhicules, trois usages.</h2>', '<h2 id="gamme-title">Trottinette électrique ou scooter pliable&nbsp;: trois modèles.</h2>'),
    ('<h2 id="videos-title">Ils les ont testés.</h2>', '<h2 id="videos-title">Tests en vidéo&nbsp;: ils les ont essayés.</h2>'),
    ('<h2 id="service-title">Le service sans stress.</h2>', '<h2 id="service-title">Réparations comprises&nbsp;: le service sans stress.</h2>'),
    ('<h2 id="faq-title">Louer une trottinette Augment&nbsp;: l’essentiel.</h2>', '<h2 id="faq-title">Location de trottinette électrique&nbsp;: vos questions.</h2>'),
    ('<h2 id="steps-title">Comment s’abonner — en moins de 5&nbsp;minutes.</h2>', '<h2 id="steps-title">Comment louer sa trottinette Augment, en moins de 5&nbsp;minutes.</h2>'),
    ('alt="Un homme en veste en jean, casque à la main, regarde son téléphone entre une trottinette Agaru et un E-scooter 360 garés dans une rue ordinaire"',
     'alt="Trottinette électrique Agaru et scooter électrique pliable E-scooter 360 garés dans la rue, un homme casque à la main"'),
])
edit('comparateur.html', [
    ('<h2 id="titre-bref">Lequel choisir&nbsp;?</h2>', '<h2 id="titre-bref">Quelle trottinette électrique Augment choisir&nbsp;?</h2>'),
    ('<h2 id="titre-comparatif">Les 14 critères, côte à côte.</h2>', '<h2 id="titre-comparatif">Comparatif Agaru Smart, Agaru Ultra et 360&nbsp;: 14 critères.</h2>'),
    ('<h2 id="titre-avis">Ce que retiennent les clients.</h2>', '<h2 id="titre-avis">Avis clients&nbsp;: ce qu’ils retiennent.</h2>'),
    ('<h2 id="titre-guides">Guides &amp; réglementation.</h2>', '<h2 id="titre-guides">Guides&nbsp;: assurance, réglementation, entretien.</h2>'),
    ('<h2 id="titre-faq">Questions fréquentes.</h2>', '<h2 id="titre-faq">Questions fréquentes sur l’Agaru et le 360.</h2>'),
])

# Deux questions de plus dans la FAQ de l'accueil (assurance, livraison) : fortes demandes de recherche
sys.path.insert(0, S + 'tools')
import faq_accueil
FAQ = list(faq_accueil.FAQ)
extra = [
    ('Faut-il une assurance pour une trottinette électrique ?',
     'Oui. En France, une trottinette électrique doit être couverte par une assurance responsabilité civile, comme tout véhicule motorisé. La couverture contre le vol proposée par Augment (2,95 €/mois) protège contre le vol, la perte et le vandalisme, mais ne remplace pas cette responsabilité civile.'),
    ('Quel est le délai de livraison ?',
     'Selon Augment, les trottinettes en stock arrivent à domicile en 3 à 4 jours ouvrés, et l’E-scooter 360 en 7 à 10 jours ouvrés.'),
]
if not any(q.startswith('Faut-il une assurance') for q, _ in FAQ):
    FAQ += extra
    io.open(S + 'tools/faq_accueil.py', 'w', encoding='utf-8').write('FAQ = ' + repr(FAQ) + '\n')
    p = S + 'index.html'
    s = io.open(p, encoding='utf-8').read()
    add = ''.join('        <details class="hfaq__item">\n          <summary><span class="hfaq__q">%s</span><span class="hfaq__icon" aria-hidden="true">+</span></summary>\n          <p class="hfaq__a">%s</p>\n        </details>\n'
                  % (q.replace(' ?', '&nbsp;?'), a) for q, a in extra)
    i = s.index('<div class="hfaq__list">'); j = s.index('      </div>\n    </div>\n  </section>', i)
    s = s[:j] + add + s[j:]
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok')
