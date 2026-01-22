# Dossier des données

Placez ici vos fichiers de données pour le projet.

## Formats supportés

- CSV (`.csv`)
- Parquet (`.parquet`)
- JSON (`.json`)
- Excel (`.xlsx`)

## Organisation recommandée

```
data/
├── raw/              # Données brutes non modifiées
├── processed/        # Données après nettoyage
└── metadata.json     # Métadonnées du projet (généré automatiquement)
```

## Fichiers générés

Le notebook génère automatiquement :
- `dataset_clean.parquet` : dataset nettoyé
- `metadata.json` : statistiques et métadonnées du traitement
