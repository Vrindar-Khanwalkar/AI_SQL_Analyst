import pandas as pd
import sqlparse


def _validate_sql(sql):
    parsed = sqlparse.parse(sql)

    if len(parsed) != 1:
        raise ValueError(
            "Only one SQL statement is allowed."
        )

    statement = parsed[0]

    if statement.get_type() != "SELECT":
        raise ValueError(
            "Only SELECT statements are allowed."
        )


def execute_sql(connection, sql):

    _validate_sql(sql)

    try:
        return pd.read_sql_query(sql, connection)

    except Exception as e:
        raise ValueError(
            f"SQL execution failed: {e}"
        )