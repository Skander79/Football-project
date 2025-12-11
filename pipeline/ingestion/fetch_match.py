from statsbombpy import sb
import pandas as pd

def fetch_matches(competition_id: int, season_id: int) -> pd.DataFrame:
    """
    Récupère les matchs StatsBomb pour une compétition + saison.
    Données BRUTES (Bronze).
    """
    df = sb.matches(competition_id=competition_id, season_id=season_id)

    # Brute copy to ensure DataFrame
    df = pd.DataFrame(df)

    return df
