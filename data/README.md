# Données du projet

Ce dossier contient les fichiers de données sources pour l'analyse de qualité de l'air.

## Fichiers présents

### Fichiers de mesures (4 jours)
- FR_E2_2025-01-01.csv
- FR_E2_2025-01-02.csv
- FR_E2_2025-01-03.csv
- FR_E2_2025-01-04.csv

Contenu de chaque fichier :
- Format : CSV séparé par point-virgule (;)
- Volume : Environ 50 000 mesures horaires par jour
- Polluants : NO2, NO, NOX as NO2, O3, PM10, PM2.5, SO2, CO, C6H6
- Colonnes : 23 (date début/fin, code site, nom site, polluant, valeur, unité, etc.)

### Fichier de métadonnées
- fr-2025-d-lcsqa-ineris-20251209.xls

Contenu :
- Format : Excel (.xls)
- Volume : 868 stations référencées
- Colonnes principales : NatlStationCode, Name, Municipality, Latitude, Longitude, AreaClassification
- Usage : Enrichissement des mesures avec coordonnées GPS et type de zone

## Ajout de fichiers supplémentaires

Le notebook supporte le chargement automatique de tous les fichiers via le pattern `FR_E2_*.csv`.

Pour ajouter d'autres jours :
1. Télécharger les fichiers depuis ATMO Grand Est (format : FR_E2_YYYY-MM-DD.csv)
2. Les placer dans ce dossier data/
3. Relancer le notebook : la cellule 2.1 détectera et combinera automatiquement tous les fichiers

Le notebook affichera automatiquement :
- Le nombre de fichiers détectés
- Le nom de chaque fichier avec son nombre de lignes
- Le volume total de données chargées

## Source des données

ATMO Grand Est - Organisme agréé de surveillance de la qualité de l'air

Données publiques disponibles sur :
- Plateforme nationale : https://www.data.gouv.fr/datasets/donnees-temps-reel-de-mesure-des-concentrations-de-polluants-atmospheriques-reglementes-1
- Format : CSV (mesures temps réel) + XLS (métadonnées stations)
