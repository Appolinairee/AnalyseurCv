from transformers import pipeline

# Définir les catégories que vous souhaitez
categories = ["santé", "compétences"]

# Charger le modèle de classification de texte
classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment", tokenizer="nlptown/bert-base-multilingual-uncased-sentiment")

# Texte à classer
text = "Je suis énergétique. Je suis développeur web."

# Prédire les scores de chaque catégorie
result = classifier(text)

# Transformer les scores en un dictionnaire de catégories avec leurs scores associés
category_scores = {category: result[0][f"label_{i}"] for i, category in enumerate(categories)}

# Afficher les scores
print(category_scores)
