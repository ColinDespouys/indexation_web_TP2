Aperçu

Ce dépôt contient deux scripts Python principaux pour la construction d'index non positionnels à partir d'un ensemble de données JSON, en particulier en analysant les titres des documents. Ces scripts facilitent la recherche et l'analyse de données à partir de titres de documents web.
Structure des Fichiers et Dossiers
Scripts

    main.py : Script d'indexation qui tokenise les titres des documents et crée un index non positionnel.
    main-lemmatized.py : Version améliorée de main.py qui applique une lemmatisation sur les titres avant de créer l'index.

Dossiers

    data : Contient les données sources utilisées par les scripts.
        crawled_urls.json : Fichier JSON contenant les URLs et titres des documents web crawlés.
    result : Dossier destiné à rassembler tous les résultats des manipulations effectuées par les scripts, y compris les index créés.

Fonctionnalités
main.py

Opérations réalisées :

    Lecture du fichier JSON (crawled_urls.json) depuis le dossier data.
    Tokenisation des titres.
    Création de l'Index Non Positionnel et association de chaque token à une liste d'indices de documents.
    Sauvegarde de l'Index dans le dossier result.

main-lemmatized.py

Ajoute une étape de lemmatisation aux opérations de main.py :

    Lemmatisation des tokens pour une indexation plus précise.
    Création et Sauvegarde de l'Index Lemmatisé dans le dossier result.

Utilisation

Assurez-vous que Python et les dépendances nécessaires (nltk, spacy, et fr_core_news_sm) sont installés.

Pour exécuter main.py :

bash

python main.py data/crawled_urls.json

Pour main-lemmatized.py :

bash

python main-lemmatized.py data/crawled_urls.json

Dépendances

    Python 3.x
    NLTK
    Spacy
    Spacy French Model (fr_core_news_sm)

Installation des Dépendances

bash

pip install nltk spacy
python -m spacy download fr_core_news_sm