import requests

# Use the same OpenRouter API key
API_KEY = "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"

def summarize_text(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""You are an expert at summarizing long documents. Please summarize the following content clearly and concisely:

{text}

Summary:"""

    payload = {
        "model": "mistralai/mistral-7b-instruct",  # Reliable for summarization
        "messages": [
            {"role": "system", "content": "You summarize academic and technical content clearly."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 1000
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"
