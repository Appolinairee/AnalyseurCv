# import openai
# client = openai.OpenAIAPI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)

import os
from openai import OpenAI

# openai.api_key = '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'
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You must classify the terms of the text into five categories: formations, expériences professionnelles, langues, informations personnelles, passions."},
    {"role": "user", "content": """
      Appolinaire Enangnon Adande
      Tél. mobile
      +229 53846658
      Email
      adandappolinaire229@gmail
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
     """},
  ]
)

print(response.choices[0].message.content)