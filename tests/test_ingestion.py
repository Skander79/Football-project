from pipeline.ingestion.fetch_competition import fetch_competitions
from db.duckdb_conn import get_connection
from pipeline.ingestion.load_bronze import create_bronze_table, load_to_duckdb
import os

DB_PATH_TEST = "data/statsbomb_test.duckdb"

print(">>> Le test démarre")

# Supprimer la DB test si elle existe
if os.path.exists(DB_PATH_TEST):
    os.remove(DB_PATH_TEST)

df = fetch_competitions()
print(f">>> Compétitions récupérées : {len(df)}")

create_bronze_table("bronze_competitions", df.head(0), test=True)
load_to_duckdb(df, "bronze_competitions", test=True)
print(">>> Chargement DuckDB OK")

# Vérifier le nombre de lignes
con = get_connection(test=True)
res = con.execute("SELECT COUNT(*) FROM bronze_competitions").fetchone()
print(">>> Lignes en base :", res[0])
con.close()

# Nettoyer après test
if os.path.exists(DB_PATH_TEST):
    os.remove(DB_PATH_TEST)
print(">>> Test terminé, DB test supprimée")
