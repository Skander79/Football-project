from db.duckdb_conn import get_connection

def create_bronze_table(table_name: str, df_model, test=False):
    con = get_connection(test=test)
    con.register("df_model", df_model)
    con.execute("""
      CREATE TABLE bronze_competitions (
      competition_id BIGINT,
      season_id BIGINT,
      country_name VARCHAR,
      competition_name VARCHAR,
      competition_gender VARCHAR,
      competition_youth BOOLEAN,
      competition_international BOOLEAN,
      season_name VARCHAR,
      match_updated TIMESTAMP,
      match_updated_360 TIMESTAMP,
      match_available_360 TIMESTAMP,
      match_available TIMESTAMP
      )
      """)

    con.close()

def load_to_duckdb(df, table_name: str, test=False):
    """
    Insère les données du DataFrame dans la table existante.
    """
    con = get_connection(test=test)
    con.register("df_tmp", df)
    con.execute(f"INSERT INTO {table_name} SELECT * FROM df_tmp")
    con.close()