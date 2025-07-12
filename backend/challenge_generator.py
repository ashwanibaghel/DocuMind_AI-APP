import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_challenge_questions(document_text):
    url = "https://openrouter.ai/api/v1/chat/completions"

    prompt = (
        "You are an AI challenge generator.\n"
        "Your task is to generate 3 logic-based, reasoning, or comprehension-style questions "
        "strictly based on the uploaded research paper. Avoid factual yes/no questions.\n\n"
        "**Example Types:** Why, How, What would happen if..., What is the implication of..., etc.\n"
        "Number each question clearly."
    )

    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Document:\n{document_text[:8000]}"}
        ],
        "temperature": 0.4
    }

    response = requests.post(url, headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"❌ API Error: {response.status_code} - {response.text}"
