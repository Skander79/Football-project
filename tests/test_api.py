from pipeline.ingestion.fetch_competition import fetch_all_matches

df = fetch_all_matches()
print(df.head())
print(len(df), "matchs récupérés")

