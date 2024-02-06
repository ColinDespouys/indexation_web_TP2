from nltk.stem.snowball import FrenchStemmer

# Créer une instance de FrenchStemmer
stemmer = FrenchStemmer()

# Exemple de stemming en français
phrases = ["L'erreur", "sauter", "facilement", "équitablement"]
stemmed_words = [stemmer.stem(word) for word in phrases]
print(f"Exemple de stemming : {stemmed_words}")

import spacy

# Charger le modèle français
nlp = spacy.load("fr_core_news_sm")

# Fonction de lemmatisation
def lemmatize(text):
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc if token.is_alpha]
    return lemmas

# Exemple d'utilisation
text = "L'erreur est humaine"
lemmas = lemmatize(text)
print(lemmas)

