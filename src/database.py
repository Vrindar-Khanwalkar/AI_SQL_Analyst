import os
import sqlite3
import pandas as pd

DATABASE_PATH = os.path.join("data", "database.db")

def connect_database():

    if not os.path.exists("data"):
        os.makedirs("data", exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    return connection


def load_csv_to_database(csv_file, table_name, connection):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, connection, if_exists='replace', index=False)
    return {"Rows": len(df), "Columns": len(df.columns)}

def list_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def close_connection(connection):
    connection.close()