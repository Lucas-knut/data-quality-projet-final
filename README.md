# Projet Qualité des Données - Analyse de la Qualité de l'Air

## Description

Ce projet applique une démarche complète de qualité des données sur les mesures de pollution atmosphérique fournies par ATMO Grand Est. L'objectif est de garantir la fiabilité des données pour une application mobile d'alerte pollution destinée aux populations sensibles.

**Problématique :** Comment garantir la fiabilité des données de qualité de l'air pour alerter efficacement les populations sensibles lors des épisodes de pollution ?

**Données analysées :**
- Source : ATMO Grand Est (organisme agréé de surveillance)
- Plateforme : https://www.data.gouv.fr/datasets/donnees-temps-reel-de-mesure-des-concentrations-de-polluants-atmospheriques-reglementes-1
- Contenu : Mesures horaires de 9 polluants (PM10, PM2.5, NO2, O3, SO2, CO, etc.)
- Période : Janvier 2025 (4 jours)
- Volume : ~200 000 mesures, 503 stations
- Format : CSV (mesures) + XLS (métadonnées stations avec GPS)

## Structure du projet

```
data_quality/
├── data/
│   ├── FR_E2_2025-01-01.csv                    # Mesures jour 1
│   ├── FR_E2_2025-01-02.csv                    # Mesures jour 2
│   ├── FR_E2_2025-01-03.csv                    # Mesures jour 3
│   ├── FR_E2_2025-01-04.csv                    # Mesures jour 4
│   ├── fr-2025-d-lcsqa-ineris-20251209.xls     # Métadonnées des stations
│   └── README.md
├── notebooks/
│   └── analyse_qualite_air.ipynb               # Notebook principal d'analyse
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Prérequis

- Docker Desktop installé et démarré
- Git (optionnel, pour cloner le projet)
- VS Code avec extension Python (optionnel, pour édition locale)

## Démarrage rapide

### 1. Lancer l'environnement Docker

```bash
# Se placer dans le répertoire du projet
cd data_quality

# Démarrer le conteneur Jupyter Lab
docker-compose up -d

# Vérifier que le conteneur est bien lancé
docker ps
```

Le serveur Jupyter Lab est accessible à l'adresse : http://localhost:8888

Note : Aucun token n'est requis pour cette configuration de développement.

### 2. Consulter le notebook d'analyse

Ouvrir dans votre navigateur :
- URL : http://localhost:8888
- Naviguer vers : `notebooks/analyse_qualite_air.ipynb`

Le notebook contient 6 sections :
1. Contexte métier et problématique
2. Profiling : analyse exploratoire
3. Règles de qualité (complétude, validité, unicité, cohérence)
4. Traitement : application des règles de nettoyage
5. Monitoring : indicateurs de qualité (KQI)
6. Conclusion et réponse à la problématique

### 3. Arrêter l'environnement

```bash
docker-compose down
```

## Utilisation avec VS Code

VS Code peut être configuré pour utiliser directement le kernel Jupyter du conteneur Docker.

### Configuration VS Code

1. **Installer l'extension Jupyter**
   - Ouvrir VS Code
   - Extensions (Cmd+Shift+X / Ctrl+Shift+X)
   - Rechercher et installer "Jupyter" (Microsoft)

2. **Ouvrir le notebook dans VS Code**
   - Ouvrir le dossier du projet dans VS Code
   - Ouvrir `notebooks/analyse_qualite_air.ipynb`

3. **Sélectionner le kernel du conteneur Docker**
   - Cliquer sur "Select Kernel" en haut à droite du notebook
   - Choisir "Existing Jupyter Server"
   - Entrer l'URL : `http://localhost:8888`
   - Laisser le champ token vide et valider

4. **Exécuter les cellules**
   - Les cellules s'exécuteront dans le conteneur Docker
   - Les modifications sont automatiquement synchronisées

### Avantages de cette configuration

- Pas d'installation Python locale requise
- Environnement isolé et reproductible
- Dépendances gérées par Docker (pandas, numpy, matplotlib, xlrd, openpyxl, etc.)
- Édition dans VS Code avec intellisense et autocomplétion
- Exécution dans le conteneur Docker

## Démarche qualité appliquée

Le projet suit une méthodologie rigoureuse en 5 étapes :

### 1. Profiling
Analyse exploratoire complète :
- Statistiques descriptives par polluant
- Détection des valeurs manquantes (4.07%)
- Identification des valeurs invalides (2.2% de valeurs négatives)
- Détection des doublons (0.34%)
- Analyse de cohérence temporelle

### 2. Définition des règles
4 dimensions de qualité avec seuils mesurables :
- Complétude : colonnes obligatoires renseignées
- Validité : valeurs dans limites physiques (0-500 µg/m³ selon polluant)
- Unicité : pas de doublons (date/station/polluant)
- Cohérence : dates logiques, durées correctes

### 3. Traitement
Pipeline de nettoyage en 5 étapes :
- Exclusion des valeurs manquantes
- Exclusion des valeurs hors limites physiques
- Dédoublonnage systématique
- Conversion des dates en datetime
- Enrichissement avec métadonnées GPS (868 stations)

### 4. Monitoring
Indicateurs clés de qualité (KQI) :
- Taux de complétude : 100%
- Taux de validité : 100%
- Taux d'unicité : 100%
- Taux de conservation : 94%
- Score global : 98.5/100

### 5. Conclusion
- 0 valeur négative restante
- 0 doublon restant
- 503 stations enrichies avec GPS et type de zone
- Dataset prêt pour production

## Résultats obtenus

### Critères de succès atteints

| Critère | Objectif | Résultat | Statut |
|---------|----------|----------|---------|
| Valeurs impossibles | 0% | 0% | Atteint |
| Complétude | > 95% | 100% | Atteint |
| Outliers non justifiés | < 1% | 0% | Atteint |
| Exploitabilité IQA | Oui | Oui | Atteint |

### Enrichissement géographique

- 503 stations de mesure validées
- 3 colonnes ajoutées : latitude, longitude, type_zone
- 100% de taux de remplissage
- Permet analyses géospatiales et alertes par zone

## Technologies utilisées

- Python 3.11
- Pandas 2.0+ : manipulation de données
- NumPy : calculs numériques
- Matplotlib / Seaborn : visualisations
- xlrd / openpyxl : lecture fichiers Excel
- Jupyter Lab : notebooks interactifs
- Docker : conteneurisation
- Great Expectations : framework qualité (prévu)

## Commandes utiles

### Gestion du conteneur

```bash
# Démarrer le conteneur
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter le conteneur
docker-compose down

# Reconstruire l'image (après modification requirements.txt)
docker-compose build
```

### Exécution dans le conteneur

```bash
# Accéder au shell du conteneur
docker exec -it data_quality_jupyter bash

# Installer un package Python
docker exec data_quality_jupyter pip install nom_package

# Lister les packages installés
docker exec data_quality_jupyter pip list

# Exécuter un script Python
docker exec data_quality_jupyter python /app/src/script.py
```

### Gestion des notebooks

```bash
# Exécuter un notebook en ligne de commande
docker exec data_quality_jupyter jupyter nbconvert --to notebook --execute /app/notebooks/analyse_qualite_air.ipynb

# Convertir notebook en HTML
docker exec data_quality_jupyter jupyter nbconvert --to html /app/notebooks/analyse_qualite_air.ipynb
```

## Architecture technique

### Isolation par conteneur

- Image : Python 3.11-slim
- Pas d'installation locale requise
- Dépendances figées dans requirements.txt
- Environnement reproductible

### Volumes Docker

```yaml
volumes:
  - ./data:/app/data           # Données partagées
  - ./notebooks:/app/notebooks # Notebooks synchronisés
  - ./src:/app/src             # Code source
  - ./tests:/app/tests         # Tests
```

Les modifications de fichiers sont automatiquement synchronisées entre l'hôte et le conteneur.

### Ports exposés

- Port 8888 : Jupyter Lab (http://localhost:8888)

## Points d'attention

### Sécurité

- Token Jupyter désactivé (développement local uniquement)
- En production : activer l'authentification par token
- Ne pas exposer le port 8888 publiquement

### Performance

- Chargement multi-fichiers automatique (glob pattern)
- Support de fichiers multiples via `FR_E2_*.csv`
- Enrichissement optimisé avec pandas merge

### Extensibilité

- Architecture modulaire (profiling / règles / traitement / monitoring)
- Pipeline reproductible et automatisable
- Prêt pour intégration CI/CD

## Auteur

Lucas Steichen
Projet final - Qualité des Données
EPSI - Janvier 2026
