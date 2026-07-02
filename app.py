import os
import gradio as gr

from src.database import (
    connect_database,
    load_csv_to_database,
    close_connection,
)
from src.schema import get_schema
from src.prompt import build_prompt
from src.llm import ask_llm
from src.sql_executor import execute_sql


def upload_dataset(file):
    connection = None

    try:
        connection = connect_database()

        table_name = os.path.splitext(os.path.basename(file.name))[0]

        metadata = load_csv_to_database(
            csv_file=file.name,
            table_name=table_name,
            connection=connection,
        )

        schema = get_schema(connection)

        status = (
            "✅ Dataset loaded successfully\n\n"
            f"Dataset : {os.path.basename(file.name)}\n"
            f"Rows     : {metadata['Rows']}\n"
            f"Columns  : {metadata['Columns']}"
        )

        return status, schema

    finally:
        if connection:
            close_connection(connection)


def analyze_question(schema, question, debug):
    connection = None
    debug_log = []

    try:
        connection = connect_database()

        debug_log.append("=" * 60)
        debug_log.append("QUESTION")
        debug_log.append(question)
        debug_log.append("")

        prompt = build_prompt(schema, question)

        if debug:
            debug_log.append("=" * 60)
            debug_log.append("PROMPT")
            debug_log.append(prompt)
            debug_log.append("")

        sql_query = ask_llm(prompt)
        print("=" * 60)
        print("RAW SQL FROM LLM")
        print(repr(sql_query))
        print("=" * 60)

        if debug:
            debug_log.append("=" * 60)
            debug_log.append("SQL GENERATED")
            debug_log.append(sql_query)
            debug_log.append("")

        result = execute_sql(connection, sql_query)

        if debug:
            debug_log.append("=" * 60)
            debug_log.append("EXECUTION")
            debug_log.append("✓ SQL executed successfully")
            debug_log.append(f"Rows Returned    : {len(result)}")
            debug_log.append(f"Columns Returned : {len(result.columns)}")

        debug_output = "\n".join(debug_log) if debug else ""

        return result, debug_output

    finally:
        if connection:
            close_connection(connection)


with gr.Blocks(title="AI SQL Analyst") as demo:

    gr.Markdown("# AI SQL Analyst")

    with gr.Row():

        with gr.Column():

            dataset = gr.File(
                label="Upload Dataset",
                file_types=[".csv"],
            )

            upload = gr.Button("Load Dataset")

            status = gr.Textbox(
                label="Dataset Status",
                interactive=False,
            )

            schema = gr.JSON(
                visible=False,
            )

        with gr.Column():

            question = gr.Textbox(
                label="Question",
                placeholder="Ask anything about your dataset...",
            )

            debug = gr.Checkbox(
                label="Debug Mode",
                value=False,
            )

            analyze = gr.Button("Analyze")

    results = gr.Dataframe(
        label="Results",
    )

    debug_output = gr.Textbox(
        label="Debug Output",
        lines=20,
        interactive=False,
        visible=True,
    )

    upload.click(
        fn=upload_dataset,
        inputs=dataset,
        outputs=[status, schema],
    )

    analyze.click(
        fn=analyze_question,
        inputs=[schema, question, debug],
        outputs=[results, debug_output],
    )

demo.launch(debug=True)