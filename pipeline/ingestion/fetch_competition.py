# pipeline/ingestion/fetch_competitions.py
from statsbombpy import sb
import pandas as pd

def fetch_competitions():
    """
    Récupère la table des compétitions disponible via StatsBomb Open Data
    et retourne un DataFrame pandas.
    """
    comps = sb.competitions()
    # comps est déjà un DataFrame via statsbombpy
    df = pd.DataFrame(comps)
    return df
