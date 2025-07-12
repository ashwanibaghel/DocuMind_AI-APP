# 🧠 DocuMind — GenAI Document Assistant

DocuMind is an AI-powered assistant that allows you to **upload any PDF or TXT document**, get a **150-word clean summary**, **ask contextual questions**, and even **test your understanding** using AI-generated challenges.  
All insights are **strictly grounded in your uploaded document**, with no hallucination.

---

## ✨ Features

- 📄 **Upload PDF/TXT Documents**
- 📝 **Auto-structured paragraph & section detection**
- 🧾 **Concise 150-word document summary**
- 💬 **Ask free-form questions from your document**
- 🎯 **Challenge Mode** — logic-based question generation + evaluation
- 📍 **Answer Justification with section & paragraph reference**
- 🎨 **Modern, clean UI built with Streamlit**

---

## 🧠 Use Cases

- Academic paper analysis  
- Research understanding  
- Business document Q&A  
- Policy and legal document insights  
- Assignment or project helpers

---

## 🛠 Tech Stack

| Layer         | Tools                                |
|---------------|--------------------------------------|
| 🧠 AI Models   | OpenRouter (Mixtral-8x7B-Instruct)   |
| 🖥 Backend     | Python, Streamlit                    |
| 📄 File Parsing| PyMuPDF, PyPDF2                     |
| 🧩 Logic       | Custom Prompt Engineering + GPT API |
| 📦 Env Mgmt    | python-dotenv, .env config           |

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/genai-assistant.git
cd genai-assistant
```
### 2. Create a virtual environment
``` base
python -m venv venv
```
### 3. Activate the environment
On Windows:
``` base
venv\Scripts\activate
```
On Mac/Linux:
``` base
source venv/bin/activate
```
### 4. Install dependencies
``` base
pip install -r requirements.txt
```
### 5. Add your OpenRouter API key
Create a file named ```.env``` in the root folder.

Add the following line:
``` base
OPENROUTER_API_KEY=Paste_Your_OpenRouter_Key_Here
```
👉 You can get a free key from https://openrouter.ai

---
## 💡 Usage Instructions
```
streamlit run app.py
```
Then, open http://localhost:8501 in your browser.

## 📁 Project Structure
```
genai-assistant/
│
├── app.py                     # Streamlit frontend
├── .env                       # Your API key goes here (not pushed)
├── requirements.txt           # Python dependencies
├── backend/
│   ├── parser.py              # Extracts raw text from file
│   ├── structure_preserver.py # Adds sections and paragraph metadata
│   ├── summarizer.py          # GPT-based summary generator
│   ├── gpt_handler.py         # Answers user questions using the doc
│   ├── challenge_generator.py # Generates logic-based questions
│   ├── challenge_evaluator.py # Evaluates user's answers
```
---
## 🧠 Credits
Created by Ashwani Baghel with ❤️ to make research & reading more intelligent.
