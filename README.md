# TP n°2 - Qualité des Données OpenFoodFacts

Projet d'analyse et d'amélioration de la qualité des données OpenFoodFacts pour une application mobile d'aide au choix alimentaire.

## 📋 Structure du projet

```
data_quality/
├── data/                    # Données brutes et traitées
│   └── food_sample.parquet  # Dataset à analyser (à ajouter)
├── notebooks/               # Notebooks Jupyter pour l'analyse
│   └── tp_qualite_donnees.ipynb
├── src/                     # Code source Python réutilisable
│   └── __init__.py
├── tests/                   # Tests unitaires (pytest)
├── Dockerfile              # Configuration Docker
├── docker-compose.yml      # Orchestration Docker
├── requirements.txt        # Dépendances Python
└── README.md              # Ce fichier
```

## 🚀 Démarrage rapide avec Docker

### Prérequis

- Docker installé sur votre machine
- Docker Compose installé

### Lancer le projet

1. **Cloner ou se placer dans le répertoire du projet**
   ```bash
   cd /Users/lucassteichen/Dev/epsi/data_quality
   ```

2. **Placer le fichier `food_sample.parquet` dans le dossier `data/`**

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
docker-compose exec jupyter jupyter nbconvert --to notebook --execute notebooks/tp_qualite_donnees.ipynb
```

**Accéder au shell du conteneur :**
```bash
docker-compose exec jupyter bash
```

**Exécuter les tests :**
```bash
docker-compose exec jupyter pytest tests/
```

## 📊 Contenu du TP

### 1. Profiling et exploration
- Chargement du dataset `food_sample.parquet`
- Exploration du schéma et statistiques de base
- Identification des variables utiles
- Création du dictionnaire de données

### 2. Audit de la qualité avec Great Expectations
- Initialisation de Great Expectations
- Création d'une suite de règles (minimum 8 expectations) :
  - Complétude (2+)
  - Unicité (1+)
  - Validité (2+)
  - Conformité (2+)
  - Cohérence (1+)
- Calcul des taux de conformité

### 3. Traitement des données
- Mise à plat des données (types basiques)
- Une ligne = un produit unique
- Séparation des informations composées
- Production du dataset `df_clean`

### 4. Valeurs aberrantes et logique métier
- Analyse des produits : 00457521, 00000131, 3760225200056
- Identification et traitement des anomalies
- Règles de détection et décisions métier

### 5. Monitoring
- Sélection de 2-3 indicateurs clés
- Définition de seuils d'alerte
- Identification des risques métier

## 📦 Éléments obligatoires

- ✅ Environnement Python isolé (Docker au lieu de venv)
- ✅ Fichier `requirements.txt`
- ✅ Fichier `README.md`
- ✅ Structuration du projet (src/ data/ ...)

## 🎁 Éléments bonus valorisés

- ⬜ Versionnement avec git (commits réguliers)
- ⬜ Tests automatisés (pytest)
- ⬜ Journalisation des traitements (logging)
- ⬜ Justification des décisions de traitement

## 🛠️ Technologies utilisées

- **Python 3.11**
- **Pandas** : manipulation de données
- **Great Expectations** : audit de qualité
- **Jupyter Lab** : notebooks interactifs
- **PyArrow** : lecture de fichiers Parquet
- **Pytest** : tests unitaires
- **Docker** : conteneurisation

## 📝 Notes

- Le projet est complètement isolé dans Docker, aucune installation locale de Python n'est requise
- Les modifications des notebooks et du code sont automatiquement synchronisées grâce aux volumes Docker
- Pour un environnement de production, il faudrait sécuriser l'accès à Jupyter Lab avec un token

## 👤 Auteur

Lucas Steichen - EPSI

## 📅 Date

Janvier 2026
