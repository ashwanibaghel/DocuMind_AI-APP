import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def gpt_answer_openrouter(document_text, user_query):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        "You are a strict document assistant.\n"
        "You will be given a document and a question.\n\n"
        "Your answer must follow these rules strictly:\n"
        "1. The answer must be grounded only in the actual uploaded document.\n"
        "2. Do NOT hallucinate or add any external information.\n"
        "3. Every answer must include a brief justification such as:\n"
        "   - 'This is supported by paragraph 2 of Section 1: Introduction'\n"
        "   - Also quote 1–2 lines directly from the relevant paragraph.\n"
        "If the document does not have enough info, say:\n"
        "'The document does not contain enough information to answer this.'"
    )


    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",  # you can change model if needed
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Document:\n{document_text[:8000]}"},
            {"role": "user", "content": f"Question:\n{user_query}"}
        ],
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"❌ API Error: {response.status_code} - {response.text}"
