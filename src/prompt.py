def build_prompt(schema, question):

    prompt = []

    prompt.append(
        "You are an expert SQLite SQL assistant."
    )

    prompt.append(
        "Generate ONLY valid SQLite SELECT queries."
    )

    prompt.append(
        "Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE or TRUNCATE statements."
    )

    prompt.append("Database Schema:")

    for table, columns in schema.items():

        prompt.append(f"Table: {table}")

        for column in columns:

            prompt.append(
                f"- {column['name']} ({column['type']})"
            )

        prompt.append("")

    prompt.append(f"User Question: {question}")

    prompt.append("Return ONLY the SQL query.")

    return "\n".join(prompt)