from docx import Document

def process_file(uploaded_file):
    if uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        content = "\n".join([para.text for para in doc.paragraphs])
        return content
    elif uploaded_file.name.endswith(".pdf"):
        return "PDF processing not implemented yet."
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    return ""
