from openai import OpenAI

class CVClassifier:
    def __init__(self):
        self.system_messages = {
            "Nom et Prénom": "Le système doit extraire uniquement le nom et le prénom du candidat du texte du CV. N'ajoutez pas vos propres mots et ne précisez pas la catégorie. Utilisez uniquement les mots du texte dans ta réponse.",
            "Adresse e-mail": "Identifiez l'adresse e-mail du candidat dans le CV. N'ajoutez pas vos propres mots et ne précisez pas la catégorie. Utilisez uniquement les mots du texte dans ta réponse.",
            "Expériences Professionnelles": "Analysez le texte du CV pour extraire les informations relatives à l'expérience professionnelle ou aux réalisations clés. N'ajoutez pas vos propres mots et ne précisez pas la catégorie. Utilisez uniquement les mots du texte dans ta réponse.",
            "Formations": "Identifiez les informations sur la formation académique du candidat. N'ajoutez pas vos propres mots et ne précisez pas la catégorie. Utilisez uniquement les mots du texte dans ta réponse.",
            "Compétences Techniques": "Examinez le texte du CV pour extraire les compétences techniques du candidat. N'ajoutez pas vos propres mots et ne précisez pas la catégorie. Utilisez uniquement les mots du texte dans ta réponse.",
            "Compétences Interpersonnelles": "Analysez le CV pour identifier les compétences interpersonnelles du candidat. N'ajoutez pas vos propres mots et ne précisez pas la catégorie. Utilisez uniquement les mots du texte dans ta réponse.",
            "Langues": "Examinez le texte pour extraire les informations sur les langues maîtrisées par le candidat. N'ajoutez pas vos propres mots et ne précisez pas la catégorie. Utilisez uniquement les mots du texte dans ta réponse."
        }

        self.client = OpenAI()
        self.results = {}

    def classify_cv_section(self, section_tag, cv_text):
        if section_tag in self.system_messages:
            system_message = self.system_messages[section_tag]
        else:
            print(f"Catégorie non reconnue : {section_tag}")
            return None

        user_message = f"[{section_tag}] {cv_text}"

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ]

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        if response and response.choices[0]:
            response = response.choices[0].message.content
            return response
        else:
            return None

    def classify_cv(self, cv_text):
        categories = ["Nom et Prénom", "Adresse e-mail", "Expériences Professionnelles", "Formations", "Compétences Techniques", "Compétences Interpersonnelles", "Langues"]

        for category in categories:
            response = self.classify_cv_section(category, cv_text)
            self.results[category] = response

    def get_results(self):
        return self.results

if __name__ == "__main__":
    
    cv_text = """
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
    """

    classifier = CVClassifier()
    classifier.classify_cv(cv_text)

    grouped_results = classifier.get_results()
    print(grouped_results)
