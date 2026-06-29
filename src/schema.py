import sqlite3

from src.database import list_tables

def get_table_columns(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    rows = cursor.fetchall()
    return [{"name": row[1],"type": row[2]} for row in rows]

def get_schema(connection):
    tables = list_tables(connection)
    schema = {}
    for table in tables:
        schema[table] = get_table_columns(connection, table )
    return schema


