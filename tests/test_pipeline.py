from src.database import (
    connect_database,
    load_csv_to_database,
    close_connection,
)
from src.schema import get_schema
from src.prompt import build_prompt
from src.llm import ask_llm
from src.sql_executor import execute_sql


CSV_PATH = "data/sample_sales.csv"
USER_QUESTION = "Show all records."


def main():
    connection = None

    try:
        print("=" * 60)
        print("STEP 1: CONNECT DATABASE")
        print("=" * 60)

        connection = connect_database()
        print("✓ Database Connected\n")

        print("=" * 60)
        print("STEP 2: LOAD CSV")
        print("=" * 60)

        load_csv_to_database(
            csv_file=CSV_PATH,
            connection=connection,
            table_name="sales",
        )
        print("✓ CSV Loaded\n")

        print("=" * 60)
        print("STEP 3: READ SCHEMA")
        print("=" * 60)

        schema = get_schema(connection)
        print(schema)
        print()

        print("=" * 60)
        print("STEP 4: BUILD PROMPT")
        print("=" * 60)

        prompt = build_prompt(schema, USER_QUESTION)
        print(prompt)
        print()

        print("=" * 60)
        print("STEP 5: GENERATE SQL")
        print("=" * 60)

        sql_query = ask_llm(prompt)
        print(sql_query)
        print()

        print("=" * 60)
        print("STEP 6: EXECUTE SQL")
        print("=" * 60)

        df = execute_sql(connection, sql_query)

        print("✓ SQL Executed Successfully")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")
        print()

        print(df)

    except Exception as e:
        print("\n❌ Pipeline Failed")
        print(f"Reason: {e}")

    finally:
        if connection:
            close_connection(connection)
            print("\n✓ Database Connection Closed")


if __name__ == "__main__":
    main()