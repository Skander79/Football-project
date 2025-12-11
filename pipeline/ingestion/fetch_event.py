from statsbombpy import sb
import pandas as pd

def fetch_events(match_id: int) -> pd.DataFrame:
    """
    Récupère les events bruts d'un match StatsBomb.
    Données BRUTES (Bronze).
    """
    df = sb.events(match_id=match_id)

    df = pd.DataFrame(df)

    return df
