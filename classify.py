import spacy

nlp = spacy.load("fr_core_news_sm")


texte_cv = """
Appolinaire Enangnon Adande Tél. mobile +229 53846658 Email adandappolinaire229@gmail
.com
Github
github
Français
courant
Anglais
intermédiaire
Goun
langue maternelle

(Esprit créatif et
travail en
profondeur)

(Leadership et
Entrepreneuriat)

(Travail en équipe)



Développeur web full stack passionné et panafricaniste chevronné, je mets mon art du
code au service du développement technologique en Afrique. Mon expertise technique
combinée à ma vision panafricaniste me pousse à créer des solutions technologiques
innovantes pour lutter contre l'indigence.
Résumé
Expériences
professionnelles
Création de site et d'application web pour structures de vente.
Agent du laboratoire de développement web de la communauté Alitcha
Alitcha est une communauté scientifique d'innovation technologique.
Formations
Octobre 2021
Institut de
Mathématique et de
Sciences Physiques
(IMSP)
3ème année de Licence Informatique
Ce cursus estudiantin est composé de deux années intenses de Classes Préparatoires
aux Grandes écoles d'Ingénieurs (CPGE) et est sanctionné par une licence spéciale en
3ème année. Etant en troisième année (2023), mon option est l'informatique.
Mai 2021
CEG 1 Avrankou
Avrankou
Baccalauréat Technologique série C (Mention Bien)
Juin 2018
CSP "La
Merveilleuse"
BEPC
Juillet 2021
En autodidactie
Formation avancée en développement web
Compétences
HTML/CSS
100%
JavaScript, ReactJS
80%
Gestion Back-end: NodeJS
80%
Gestion de bases de données:
MongoDB, MySQL
80%
Langage C
100%
Langues
Qualités
"""

# Catégories prédéfinies avec les labels NER associés
categories_ner = {
    "informations_personnelles": ["PER"],
    "objectif_professionnel": ["OCC"],
    "expérience_professionnelle": ["ORG", "LOC", "DATE"],
    "formation": ["EDU", "ORG", "LOC", "DATE"],
    "compétences_techniques": ["TECH"],
    "compétences_interpersonnelles": ["SKILL"],
    "langues": ["LANG"],
    "certifications": ["CERT", "ORG", "DATE"],
    "centres_d_interet": ["INTEREST"],
    "références": ["PER"],
    "portfolio_projets_personnels": ["URL"],
    "réseaux_sociaux": ["URL"]
}

# Dictionnaire pour stocker les résultats par catégorie
results = {category: [] for category in categories_ner}

# Extraction des entités nommées pertinentes pour chaque catégorie
doc = nlp(texte_cv)
for ent in doc.ents:
    for category, ner_labels in categories_ner.items():
        if ent.label_ in ner_labels:
            results[category].append(ent.text)
            break

# Afficher les résultats
for category, entities in results.items():
    print(f"Catégorie: {category}")
    for entity in entities:
        print(f" - {entity}")
    print("\n")
