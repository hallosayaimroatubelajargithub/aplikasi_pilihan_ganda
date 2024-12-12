from docx import Document

def process_file(uploaded_file):
    # Example for handling DOCX (other formats like PDF can use libraries like PyPDF2)
    if uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        content = "\n".join([para.text for para in doc.paragraphs])
        return content
    elif uploaded_file.name.endswith(".pdf"):
        # Use libraries like PyPDF2 to extract PDF text
        pass
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    return ""
