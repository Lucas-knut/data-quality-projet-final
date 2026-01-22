# Projet Final - Qualité des Données - EPSI

Infrastructure Docker pour le projet final de qualité des données (groupe 4-5 personnes).

## Structure du projet

```
data_quality/
├── data/                    # Données brutes et traitées
│   └── dataset.csv          # Dataset à analyser (à ajouter)
├── notebooks/               # Notebooks Jupyter pour l'analyse
│   └── projet_qualite_donnees.ipynb    # Notebook principal
├── src/                     # Code source Python réutilisable
│   ├── __init__.py
│   ├── data_cleaning.py
│   └── quality_validation.py
├── tests/                   # Tests unitaires (pytest)
├── Dockerfile              # Configuration Docker
├── docker-compose.yml      # Orchestration Docker
├── requirements.txt        # Dépendances Python
└── README.md              # Ce fichier
```

## Démarrage rapide avec Docker

### Prérequis

- Docker installé sur votre machine
- Docker Compose installé

### Lancer le projet

1. **Cloner ou se placer dans le répertoire du projet**
   ```bash
   cd /Users/lucassteichen/Dev/epsi/data_quality
   ```

2. **Placer votre dataset dans le dossier `data/`**
   ```bash
   # Exemple : dataset.csv, dataset.parquet, etc.
   ```

3. **Construire et lancer le conteneur Docker**
   ```bash
   docker-compose up --build
   ```

4. **Accéder à Jupyter Lab**
   - Ouvrir votre navigateur à l'adresse : http://localhost:8888
   - Aucun token requis (désactivé pour le développement local)

5. **Arrêter le conteneur**
   ```bash
   docker-compose down
   ```

### Commandes utiles

**Reconstruire l'image après modification du requirements.txt :**
```bash
docker-compose build
```

**Exécuter un notebook en ligne de commande :**
```bash
docker-compose exec jupyter jupyter nbconvert --to notebook --execute notebooks/projet_qualite_donnees.ipynb
```

**Accéder au shell du conteneur :**
```bash
docker-compose exec jupyter bash
```

**Exécuter les tests :**
```bash
docker-compose exec jupyter pytest tests/
```

## Objectif du projet

Appliquer une démarche complète de qualité des données sur un dataset de votre choix dans un contexte réaliste.

### Attendus
- Définir un **contexte métier** et une **problématique claire**
- Réaliser un **profiling** et identifier les problèmes de qualité
- Définir des **règles de qualité** avec des seuils mesurables
- Implémenter les **traitements** (correction, exclusion, enrichissement)
- Mettre en place un **monitoring** de la qualité avec indicateurs
- Conclure par une **réponse claire** à la problématique

### Livrables
- **Présentation** : slides synthétiques
- **Notebook/code** : analyse complète et documentée → [projet_qualite_donnees.ipynb](notebooks/projet_qualite_donnees.ipynb)
- **Données préparées** : dataset nettoyé + métadonnées
- **Reproductibilité** : environnement Docker (déjà configuré !)

### Organisation
- **Groupe** : 4-5 personnes
- **Sujet** : libre (pas OpenFoodFacts)
- **Dataset** : au choix (voir suggestions ci-dessous)

## Suggestions de datasets

Choisissez un dataset avec des problèmes de qualité réels :

**Santé :**
- Vaccinations COVID, hospitalisations

**Transport :**
- Accidents routiers, Vélib/vélos partagés

**Immobilier :**
- DVF (ventes immobilières), Airbnb

**Environnement :**
- Qualité de l'air, stations météo

**Finance :**
- Transactions, crypto-monnaies

**Autres :**
- Données publiques (data.gouv.fr)
- Kaggle datasets
- APIs ouvertes (Twitter, GitHub, etc.)

## Éléments du projet

### Obligatoires
- Environnement Python isolé (Docker)
- Fichier `requirements.txt`
- Fichier `README.md`
- Structuration du projet (src/ data/ ...)

### Bonus valorisés
- Versionnement avec git (commits réguliers)
- Tests automatisés (pytest)
- Journalisation des traitements (logging)
- Justification des décisions de traitement

## Technologies utilisées

- **Python 3.11**
- **Pandas** : manipulation de données
- **Great Expectations** : audit de qualité
- **Jupyter Lab** : notebooks interactifs
- **PyArrow** : lecture de fichiers Parquet
- **Pytest** : tests unitaires
- **Docker** : conteneurisation

## Notes

- Le projet est complètement isolé dans Docker, aucune installation locale de Python n'est requise
- Les modifications des notebooks et du code sont automatiquement synchronisées grâce aux volumes Docker
- Pour un environnement de production, il faudrait sécuriser l'accès à Jupyter Lab avec un token

## Auteur

Lucas Steichen - EPSI

## Date

Janvier 2026
