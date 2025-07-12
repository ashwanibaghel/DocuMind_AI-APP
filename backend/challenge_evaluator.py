import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
def evaluate_user_response(document_text, question, user_answer):
    url = "https://openrouter.ai/api/v1/chat/completions"

    prompt = (
        "You are an expert evaluator.\n"
        "Evaluate the user's answer based on the actual content of the given research paper.\n\n"
        "Steps:\n"
        "1. Compare the user's answer to the expected concept in the paper\n"
        "2. Provide feedback: Correct / Partially correct / Incorrect\n"
        "3. Add justification from the document with paragraph/section reference.\n\n"
        "4. and then you give the correct answer if answer are incorrect.\n"
        "Be strict. Only use the document to judge."
    )

    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Document:\n{document_text[:8000]}"},
            {"role": "user", "content": f"Question: {question}\nUser Answer: {user_answer}"}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"❌ API Error: {response.status_code} - {response.text}"
