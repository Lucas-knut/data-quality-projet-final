"""
Tests unitaires pour le module de nettoyage des données.
"""

import pytest
import pandas as pd
from src.data_cleaning import load_data, clean_data


def test_load_data():
    """Test du chargement des données."""
    # TODO: Implémenter le test
    pass


def test_clean_data():
    """Test du nettoyage des données."""
    # Créer un DataFrame de test
    df_test = pd.DataFrame({
        'code': ['123', '456'],
        'product_name': ['Produit A', 'Produit B']
    })
    
    # TODO: Implémenter le test
    df_clean = clean_data(df_test)
    
    assert len(df_clean) == 2
    # Ajouter d'autres assertions
