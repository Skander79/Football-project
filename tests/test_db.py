from db.duckdb_conn import get_conn

conn = get_conn()

# Vérifie que la base fonctionne
result = conn.execute("SELECT 1").fetchall()
print("Connexion OK :", result)

conn.close()

