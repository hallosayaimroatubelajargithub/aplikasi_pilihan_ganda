import re

def parse_questions(content):
    questions = []
    raw_questions = content.split("\n\n")
    for raw_question in raw_questions:
        lines = raw_question.split("\n")
        if len(lines) > 2:
            question_text = lines[0].strip()
            options = [line.strip() for line in lines[1:-1]]
            answer = re.search(r"Jawaban: ([A-D])", lines[-1])
            if answer:
                questions.append({
                    "question": question_text,
                    "options": options,
                    "answer": options[ord(answer.group(1)) - 65]  # Convert A-D to index
                })
    return questions
