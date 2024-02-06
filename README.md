# Aperçu

Ce dépôt contient deux scripts Python principaux pour la construction d'index non positionnels à partir d'un ensemble de données JSON, en particulier en analysant les titres des documents. Ces scripts facilitent la recherche et l'analyse de données à partir de titres de documents web.

# Structure des Fichiers et Dossiers

# Scripts

main.py : Script d'indexation qui tokenise les titres des documents et crée un index non positionnel.

main_lemmatized.py : Version améliorée de main.py qui applique une lemmatisation sur les titres avant de créer l'index.

# Dossiers

data : Contient crawled_urls.json, un fichier JSON contenant les URLs et titres des documents web crawlés.

result : Dossier destiné à rassembler tous les résultats des manipulations effectuées par les scripts, y compris les index créés.

# Fonctionnalités

### main.py

Opérations réalisées :

1. Lecture du fichier JSON (crawled_urls.json) depuis le dossier data.
2. Tokenisation des titres.
3. Création de l'Index Non Positionnel et association de chaque token à une liste d'indices de documents.
4. Sauvegarde de l'Index dans le dossier result.

### main_lemmatized.py

Ajoute une étape de lemmatisation aux opérations de main.py :

Lemmatisation des tokens pour une indexation plus précise.

Création et Sauvegarde de l'Index Lemmatisé dans le dossier result.

### Analyse de Similarité (similarity.py)

Ce script évalue la similarité entre les index non positionnels générés par les deux méthodes principales (main.py et main-lemmatized.py). Il utilise la similarité de Jaccard pour comparer les ensembles de documents associés à chaque token dans les deux index, calculant ainsi une moyenne de similarité globale. Le script identifie également les tokens uniques à chaque index et les différences dans les listes de documents pour les tokens communs.

### Test de Stemming et Lemmatisation (test_stemmer.py)

Démontre l'utilisation du FrenchStemmer de NLTK pour le stemming en français et de Spacy pour la lemmatisation. Ce script fournit des exemples pratiques pour observer les différences entre stemming et lemmatisation sur des phrases en français, illustrant l'efficacité de chaque méthode dans la réduction des mots à leur forme racine ou lemme.

# Utilisation

Assurez-vous que Python et les dépendances nécessaires (nltk, spacy, et fr_core_news_sm) sont installés.

Pour exécuter main.py :

python main.py data/crawled_urls.json

Pour main_lemmatized.py :

python main_lemmatized.py data/crawled_urls.json

### Dépendances

Python 3.x

NLTK

Spacy

Spacy French Model (fr_core_news_sm)

### Installation des Dépendances

pip install nltk spacy

python -m spacy download fr_core_news_sm