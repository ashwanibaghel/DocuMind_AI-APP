import streamlit as st
from backend.parser import extract_text_from_file
from backend.summarizer import gpt_summary_openrouter
from backend.gpt_handler import gpt_answer_openrouter
from backend.structure_preserver import add_sections_and_paragraphs
from backend.challenge_generator import generate_challenge_questions
from backend.challenge_evaluator import evaluate_user_response

st.set_page_config(page_title="DocuMind | Document Intelligence", layout="wide")

st.markdown("""
    <style>
        .block-container {padding: 1rem 2rem;}
        h1, h2, h3, h4 {color: #2c3e50;}
        .stButton > button {font-size: 16px; padding: 0.6em 1.2em; background-color: #007bff; color: white; border: none; border-radius: 5px;}
        .summary-box {
            border: 1px solid #007bff;
            padding: 15px;
            border-radius: 5px;
            background-color: #f8f9fa;
            color: #1a1a1a;
        }
        .question-box {
            border-left: 4px solid #007bff;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #f0f0f0;
            border-radius: 5px;
            color: #1a1a1a;
        }
        .feedback-box {
            background-color: #e9f7ef;
            padding: 10px;
            border-radius: 5px;
            color: #1a1a1a;
        }
        .footer-note {
            text-align: center;
            margin-top: 50px;
            color: #888;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>DocuMind: Document Intelligence Assistant</h1>", unsafe_allow_html=True)

st.sidebar.title("Upload Document")
uploaded_file = st.sidebar.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("Reading and structuring your document..."):
        raw_text = extract_text_from_file(uploaded_file)
        structured_text = add_sections_and_paragraphs(raw_text)

    mode = st.sidebar.selectbox("Choose a mode", ["Summary", "Ask Anything", "Challenge Me"])

    if mode == "Summary":
        st.subheader("Document Summary")
        if st.button("Show Summary"):
            with st.spinner("Generating summary..."):
                summary = gpt_summary_openrouter(structured_text)
            st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

        with st.expander("📄 View Full Structured Document"):
            st.text_area("Structured Document", structured_text, height=400)

    elif mode == "Ask Anything":
        st.subheader("Ask Anything")
        question = st.text_input("Enter your question about the document")
        if st.button("Submit Question"):
            if question:
                with st.spinner("Generating answer..."):
                    answer = gpt_answer_openrouter(structured_text, question)
                st.markdown(f"<div class='feedback-box'><strong>Answer:</strong> {answer}</div>", unsafe_allow_html=True)
            else:
                st.error("Please enter a question.")

    elif mode == "Challenge Me":
        st.subheader("Challenge Mode")
        if "questions" not in st.session_state:
            st.session_state.questions = []
            st.session_state.answers = []
            st.session_state.feedbacks = {}

        if not st.session_state.questions:
            if st.button("Start Challenge"):
                with st.spinner("Generating challenge questions..."):
                    questions = generate_challenge_questions(structured_text).split("\n")[:3]
                    st.session_state.questions = questions
                    st.session_state.answers = ["" for _ in questions]
                st.rerun()
        else:
            for i, q in enumerate(st.session_state.questions, 1):
                st.markdown(f"<div class='question-box'>**Question {i}**: {q}</div>", unsafe_allow_html=True)
                user_answer = st.text_area(f"Your answer for Question {i}", value=st.session_state.answers[i-1], key=f"answer_{i}")
                if st.button(f"Submit Answer {i}", key=f"submit_{i}"):
                    st.session_state.answers[i-1] = user_answer
                    if user_answer.strip():
                        feedback_key = f"feedback_{i}"
                        with st.spinner("Evaluating answer..."):
                            feedback = evaluate_user_response(structured_text, q, user_answer)
                            st.session_state[feedback_key] = feedback
                feedback_key = f"feedback_{i}"
                if st.session_state.get(feedback_key):
                    st.markdown(f"<div class='feedback-box'><strong>Feedback:</strong> {st.session_state[feedback_key]}</div>", unsafe_allow_html=True)

        st.markdown("<div class='footer-note'>Made with ❤️ by Ashwani Baghel | Powered by Streamlit</div>", unsafe_allow_html=True)

else:
    st.info("Please upload a document to begin.")
