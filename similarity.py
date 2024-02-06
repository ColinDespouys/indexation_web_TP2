import json

# Fonction pour charger un index à partir d'un fichier JSON
def load_index(json_path):
    with open(json_path, 'r') as file:
        return json.load(file)

# Fonction pour calculer la similarité de Jaccard
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union != 0 else 0

# Charger les index
lemmatized_index = load_index('results/lemmatized.title.non_pos_index.json')
non_lemmatized_index = load_index('results/title.non_pos_index.json')

# Calculer la similarité pour chaque token commun
similarities = []
for token in lemmatized_index:
    if token in non_lemmatized_index:
        sim = jaccard_similarity(set(lemmatized_index[token]), set(non_lemmatized_index[token]))
        similarities.append(sim)

# Calculer la moyenne des similarités
average_similarity = sum(similarities) / len(similarities) if similarities else 0

print(f"Moyenne de similarité de Jaccard : {average_similarity}")

# Identifier les tokens uniques à chaque index
unique_to_lemmatized = set(lemmatized_index.keys()) - set(non_lemmatized_index.keys())
unique_to_non_lemmatized = set(non_lemmatized_index.keys()) - set(lemmatized_index.keys())

# Identifier les différences dans les listes de documents pour les tokens communs
differences_in_docs = {}
for token in set(lemmatized_index.keys()).intersection(set(non_lemmatized_index.keys())):
    lemmatized_docs = set(lemmatized_index[token])
    non_lemmatized_docs = set(non_lemmatized_index[token])
    if lemmatized_docs != non_lemmatized_docs:
        differences_in_docs[token] = {
            'lemmatized': list(lemmatized_docs - non_lemmatized_docs),
            'non_lemmatized': list(non_lemmatized_docs - lemmatized_docs)
        }

# Afficher les résultats
print(f"Tokens uniques à l'index lemmatisé: {unique_to_lemmatized}")
print(f"Tokens uniques à l'index non lemmatisé: {unique_to_non_lemmatized}")
print(f"Differences dans les documents pour les tokens communs: {differences_in_docs}")
