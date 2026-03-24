import requests

import os
API_KEY = os.getenv("OPENROUTER_API_KEY")


# =========================
# 🔹 OPENROUTER (API)
# =========================
def generate_answer(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an AI assistant.

Answer ONLY from the provided context.
If the answer is not present, say "I don't know".

Format the answer STRICTLY as:
- Each point on a new line
- Use bullet points
- Keep it concise
- Do not add extra information

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    data = response.json()
    print("API Response:", data)

    if "choices" not in data:
        return f"API Error: {data}"

    return data["choices"][0]["message"]["content"]


# =========================
# 🔹 OLLAMA (LOCAL LLM)
# =========================
def generate_answer_local(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an AI assistant.

Answer ONLY from the provided context.
If the answer is not present, say "I don't know".

Format the answer STRICTLY as:
- Each point on a new line
- Use bullet points
- Keep it concise

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data.get("response", "No response from local model")

    except Exception as e:
        return f"Ollama Error: {str(e)}"