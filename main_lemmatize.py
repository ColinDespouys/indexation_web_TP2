import json
import spacy
from collections import defaultdict
from nltk.tokenize import word_tokenize

# Charger le modèle français de Spacy
nlp = spacy.load("fr_core_news_sm")

# Fonction pour charger les données JSON
def load_data(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data

# Fonction pour tokeniser et appliquer la lemmatisation
def tokenize_and_lemmatize(text):
    doc = nlp(text.lower())
    lemmatized_tokens = [token.lemma_ for token in doc if token.is_alpha]
    return lemmatized_tokens

# Créer un index non positionnel avec lemmatisation
def create_lemmatized_non_pos_index(data):
    index = defaultdict(list)
    for i, entry in enumerate(data):
        tokens = tokenize_and_lemmatize(entry['title'])
        for token in tokens:
            if i not in index[token]:
                index[token].append(i)
    return index

# Fonction pour écrire les données dans un fichier JSON
def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Utilisation des fonctions
json_path = 'crawled_urls.json'
data = load_data(json_path)

# Index non positionnel avec lemmatisation
lemmatized_non_pos_index = create_lemmatized_non_pos_index(data)
write_json(lemmatized_non_pos_index, 'lemmatized.title.non_pos_index.json')
