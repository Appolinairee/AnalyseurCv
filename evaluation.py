import spacy
from openai import OpenAI

class CVEvaluator:
    
    def __init__(self):
        self.nlp = spacy.load("fr_core_news_md")
        self.client = OpenAI()


    def evaluate_cv(self, cv_text, recruiter_query):
        total_score = 0

        for category, criteria in recruiter_query.items():
            category_text = getattr(cv_text, category, "")
            
            if category_text:
                category_score = self.evaluate_category(category_text, category, criteria)

                if category_score is not None:
                    total_score += category_score

        return total_score
        
        
    def evaluate_category(self, cv_text, category, criteria):
        cv_elements = cv_text.split('\n')

        total_score = 0

        for cv_element in cv_elements:
            spacy_score = self.evaluate_spacy_similarity(cv_element, criteria)
            chatgpt_score = self.evaluate_chatgpt_similarity(cv_element, category, criteria)

            if spacy_score is not None and chatgpt_score is not None:
                combined_score = self.combine_scores(spacy_score, chatgpt_score)
                total_score += combined_score

        return total_score

        

    def evaluate_spacy_similarity(self, cv_text, criteria):
        doc_cv = self.nlp(cv_text)
        doc_criteria = self.nlp(criteria)

        return doc_cv.similarity(doc_criteria)


    def evaluate_chatgpt_similarity(self, cv_text, category, criteria):
        system_message = f"[{category}] Calculez la similarité entre le texte fourni et les critères suivants : {criteria}. Renvoyez uniquement un nombre entre 0 et 1 sans autres mots.Tu n'enverras pas de texte. Juste le nombre. Prends en compte les mots synonymes et aussi les sigles"
        user_message = cv_text

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ]

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        if response and response.choices[0]:
            
            cleaned_response = response.choices[0].message.content.strip()
            print(response.choices[0].message.content)
            
            try:
                # Convertir la réponse en un nombre entre 0 et 1
                similarity_score = float(cleaned_response)
                
                # Assurer que le score est dans la plage [0, 1]
                similarity_score = max(0, min(1, similarity_score))

                return similarity_score
            except ValueError:
                return None
        else:
            return None



    def combine_scores(self, spacy_score, chatgpt_score, spacy_weight=0.7, chatgpt_weight=0.3):
        combined_score = spacy_weight * spacy_score + chatgpt_weight * chatgpt_score
        return combined_score

    def get_category_content(self, cv_text, category):
        pass
    
    
cv_text = "Je suis développeur web Javascript."
category = "Expériences Professionnelles"
criteria = "Je suis développeur web Javascript"

evaluator = CVEvaluator()
similarity_score = evaluator.evaluate_spacy_similarity(cv_text, criteria)

# Affichez le résultat
print(f"Similarité entre le CV et les critères : {similarity_score}")