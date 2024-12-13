import streamlit as st
import sys
import os

# Tambahkan direktori utama proyek ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.utils.file_handler import process_file
from app.utils.question_parser import parse_questions
from app.utils.api_client import validate_answer_with_llm


st.set_page_config(page_title="Aplikasi Pilihan Ganda", layout="wide")

def main():
    st.title("Aplikasi Pilihan Ganda")
    st.markdown('<link rel="stylesheet" href="app/static/style.css">', unsafe_allow_html=True)
    
    st.header("Upload File Soal")
    uploaded_file = st.file_uploader("Upload file (docx, PDF, txt)", type=["docx", "pdf", "txt"])

    if uploaded_file:
        content = process_file(uploaded_file)
        questions = parse_questions(content)
        
        if questions:
            st.header("Jawab Pertanyaan")
            user_answers = {}
            for idx, question in enumerate(questions):
                st.write(f"**{idx+1}. {question['question']}**")
                user_answers[idx] = st.radio("", question['options'], key=f"q{idx}")

            if st.button("Submit"):
                score = 0
                st.header("Hasil dan Pembenaran")
                for idx, question in enumerate(questions):
                    user_answer = user_answers[idx]
                    llm_response = validate_answer_with_llm(question['question'], user_answer, question['answer'])
                    
                    st.write(f"**{idx+1}. {question['question']}**")
                    st.write(f"- Jawaban Anda: **{user_answer}**")
                    if llm_response["is_correct"]:
                        st.write(":white_check_mark: **Benar!**")
                        score += 1
                    else:
                        st.write(f":x: **Salah**, Jawaban yang benar adalah: **{question['answer']}**")
                        st.write(f"_Catatan AI_: {llm_response['explanation']}")
                
                st.success(f"Skor Anda: {score}/{len(questions)}")
        else:
            st.error("Tidak ada soal ditemukan dalam file.")
    else:
        st.info("Silakan upload file terlebih dahulu.")

if __name__ == "__main__":
    main()
