# backend/parser.py
import fitz  # PyMuPDF

def extract_text_from_file(file):
    if file.name.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif file.name.endswith('.txt'):
        return extract_text_from_txt(file)
    else:
        return "❌ Unsupported file format. Please upload PDF or TXT."

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_txt(file):
    return file.read().decode("utf-8")
