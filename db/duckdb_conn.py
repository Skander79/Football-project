import duckdb
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "data/statsbomb.duckdb")
DB_PATH_TEST = os.getenv("DB_PATH_TEST", "data/statsbomb_test.duckdb")

def get_connection(test: bool = False):
    if test:
        return duckdb.connect(DB_PATH_TEST)
    return duckdb.connect(DB_PATH)

