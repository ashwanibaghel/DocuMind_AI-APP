import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def gpt_summary_openrouter(document_text):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        "You are a summarizer. Summarize the given document in **exactly 150 words or fewer**.\n"
        "The summary must be clean, clear, and reflect the core content."
        "Do NOT include any paragraph or section reference in the summary.\n"
        "the given advice follow the strictly and not given the summary more than 150 words."
    )

    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Document:\n{document_text[:8000]}"}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"❌ API Error: {response.status_code} - {response.text}"
