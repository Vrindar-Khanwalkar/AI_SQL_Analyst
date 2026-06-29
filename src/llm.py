from ollama import chat

MODEL_NAME = "phi3"


def ask_llm(prompt):

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert SQLite SQL assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0
        }
    )

    return response["message"]["content"].strip()