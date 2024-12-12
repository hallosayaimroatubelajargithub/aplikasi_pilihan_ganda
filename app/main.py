import streamlit as st
from utils.file_handler import process_file
from utils.question_parser import parse_questions

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
                correct_count = 0
                feedback = []

                for idx, question in enumerate(questions):
                    correct = user_answers[idx] == question['answer']
                    correct_count += correct
                    feedback.append({
                        "question": question['question'],
                        "user_answer": user_answers[idx],
                        "correct_answer": question['answer'],
                        "is_correct": correct
                    })
                
                st.success(f"Skor Anda: {correct_count}/{len(questions)}")

                st.header("Pembenaran Jawaban")
                for item in feedback:
                    st.write(f"**{item['question']}**")
                    st.write(f"- Jawaban Anda: **{item['user_answer']}**")
                    if item['is_correct']:
                        st.write(":white_check_mark: **Benar**")
                    else:
                        st.write(f":x: **Salah**, Jawaban yang benar adalah: **{item['correct_answer']}**")
        else:
            st.error("Tidak ada soal ditemukan dalam file.")
    else:
        st.info("Silakan upload file terlebih dahulu.")

if __name__ == "__main__":
    main()
