import os
import fitz  # pymupdf
from pptx import Presentation
from docx import Document
import pytesseract
from PIL import Image
import spacy
from spacy.training.example import Example

# Charger le modèle spaCy pré-entraîné pour le français
nlp = spacy.load("fr_core_news_sm")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Exemple de données d'entraînement
training_data = [
    ("Je m'appelle John Doe et je vis à Paris. Mon numéro de téléphone est 0123456789.", {"entities": [(15, 24, "informations_personnelles")]}),
    ("À la recherche d'un poste de développeur web expérimenté.", {"entities": [(32, 48, "objectif_professionnel")]}),
    ("Développeur Full Stack chez ABC Corp. de janvier 2018 à juillet 2021. Responsable du développement d'applications web.", {"entities": [(0, 22, "expérience_professionnelle"), (38, 58, "expérience_professionnelle"), (83, 117, "expérience_professionnelle")]}),
    ("Master en Informatique à l'Université XYZ, 2017-2019.", {"entities": [(0, 37, "formation"), (41, 51, "formation")]}),
    ("Compétences techniques : Python, JavaScript, React, SQL.", {"entities": [(21, 27, "compétences_techniques"), (29, 38, "compétences_techniques"), (40, 45, "compétences_techniques"), (47, 50, "compétences_techniques")]}),
    ("Excellentes compétences en communication et capacité à travailler en équipe.", {"entities": [(13, 32, "compétences_interpersonnelles"), (42, 57, "compétences_interpersonnelles")]}),
    ("Langues : Français (courant), Anglais (intermédiaire).", {"entities": [(9, 16, "langues"), (28, 35, "langues")]}),
    ("Certification AWS Certified Developer - Associate, obtenu en juin 2020.", {"entities": [(13, 60, "certifications"), (70, 79, "certifications"), (82, 92, "certifications")]}),
    ("Centres d'intérêt : Lecture, Cyclisme.", {"entities": [(21, 28, "centres_d_interet"), (30, 38, "centres_d_interet")]}),
    ("Références disponibles sur demande.", {"entities": [(0, 8, "références")]}),
]

# Convertir les exemples en format spaCy
spacy_training_data = []
for text, annotations in training_data:
    doc = nlp(text)
    example = Example.from_dict(doc, annotations)
    spacy_training_data.append(example)

# Entraîner le modèle spaCy
random_seed = 1  # Seed pour la reproductibilité
spacycode.util.fix_random_seed(random_seed)
spacycode.util.set_random_seed(random_seed)
optimizer = nlp.begin_training()

# Itérations d'entraînement
epochs = 10
for epoch in range(epochs):
    losses = {}
    # Mélanger les données d'entraînement pour chaque époque
    spacycode.util.fix_random_seed(random_seed)
    random_seed += 1
    # Entraîner le modèle avec les données d'entraînement
    for example in spacy_training_data:
        text = example[0]
        entities = example[1]['entities']
        biluo_tags = spacycode.training.offsets_to_biluo_tags(nlp.make_doc(text), entities)
        print(f"Texte: {text}")
        print(f"Entités: {entities}")
        print(f"Tags BIOUL: {biluo_tags}")
        nlp.update([example], drop=0.5, losses=losses)
    print(losses)

# Afficher les résultats
for ent in doc.ents:
    print(f"Texte: {ent.text}, Label: {ent.label_}")


# Processus de segmentation en phrases
combined_text = """Appolinaire Enangnon Adande Tél. mobile +229 53846658 Email adandappolinaire229@gmail
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
Qualités"""

doc = nlp(combined_text)

categories = {
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

results = {category: [] for category in categories}

# Extraction des entités nommées pertinentes pour chaque catégorie
results = {category: [] for category in categories}
for ent in doc.ents:
    for category, ner_labels in categories.items():
        if ent.label_ in ner_labels:
            results[category].append(ent.text)
            break

# Afficher les résultats
for category, entities in results.items():
    print(f"Catégorie: {category}")
    for entity in entities:
        print(f" - {entity}")
    print("\n")