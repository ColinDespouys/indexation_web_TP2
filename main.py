import json
import re
from collections import defaultdict, Counter

# 1. Lire le fichier JSON
def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 2. Tokeniser les titres
def tokenize(text):
    # Supprimer la ponctuation et convertir en minuscules
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

# 3. Créer l'index non positionnel
def create_non_pos_index(data):
    index = defaultdict(list)
    for i, entry in enumerate(data):
        tokens = tokenize(entry['title'])
        for token in tokens:
            if i not in index[token]:
                index[token].append(i)
    return index

# 4. Calculer les statistiques
def calculate_statistics(data):
    stats = {
        "Nombre total de document": len(data),
        "Nombre de token par champs": {},
        "Moyenne du nombre de token par champs": {}
    }
    
    for field in ['url', 'title', 'content', 'h1']:
        token_counts = Counter()
        for entry in data:
            tokens = tokenize(entry.get(field, ''))
            token_counts.update(tokens)
        stats["Nombre de token par champs"][field] = sum(token_counts.values())
        
    for field in ['url', 'title', 'content', 'h1']:
        stats['Moyenne du nombre de token par champs'][field] = stats["Nombre de token par champs"][field] / len(data)
    return stats


# 5. Écrire les fichiers JSON de sortie
def write_json(data, filename):
    # Convertir uniquement les sets en listes pour la sérialisation JSON
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, set):
                data[key] = list(value)
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    json_path = 'TP2/data/crawled_urls.json'
    data = load_data(json_path)
    non_pos_index = create_non_pos_index(data)
    metadata = calculate_statistics(data)

    write_json(non_pos_index, 'TP2/results/title.non_pos_index.json')
    write_json(metadata, 'TP2/results/metadata.json')
