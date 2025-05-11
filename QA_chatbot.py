import requests

# Use your OpenRouter API key
API_KEY = "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"

def ask_question(question, context):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""You are a helpful assistant. Use the following context from a PDF to answer the user's question.

Context:
{context}

Question:
{question}

Answer:"""

    payload = {
        "model": "mistralai/mistral-7b-instruct",  # You can change this to any OpenRouter-supported model
        "messages": [
            {"role": "system", "content": "You answer questions based on PDF content accurately and concisely."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"❌ Error: {response.status_code} - {response.text}"
