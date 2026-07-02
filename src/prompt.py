def build_prompt(schema, question):
    prompt = []

    prompt.append(
        "You are an expert SQLite SQL generator.\n"
        "Your ONLY task is to convert a natural language question into ONE valid SQLite SELECT query."
    )

    prompt.append("\nDATABASE SCHEMA:")

    for table, columns in schema.items():
        prompt.append(f"\nTable: {table}")
        for column in columns:
            prompt.append(f"- {column['name']} ({column['type']})")

    prompt.append("\nRULES:")
    prompt.append("- Generate EXACTLY ONE SQL statement.")
    prompt.append("- The statement MUST be a SELECT query.")
    prompt.append("- Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE or TRUNCATE.")
    prompt.append("- Never generate more than one SQL statement.")
    prompt.append("- Never explain your answer.")
    prompt.append("- Never include markdown.")
    prompt.append("- Never wrap the SQL inside ```sql```.")
    prompt.append("- Never generate sample queries.")
    prompt.append("- Never generate alternative queries.")
    prompt.append("- Only use tables and columns present in the schema.")
    prompt.append("- Do NOT invent tables or columns.")
    prompt.append("- If the question cannot be answered using the schema, return exactly: INVALID_QUERY")
    prompt.append("- Return ONLY the raw SQL statement ending with a semicolon.")

    prompt.append(f"\nUSER QUESTION:\n{question}")

    prompt.append("\nSQL:")

    return "\n".join(prompt)