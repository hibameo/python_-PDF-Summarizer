import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    if uploaded_file is not None:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())  # Save uploaded file temporarily
        doc = fitz.open("temp.pdf")  # Open saved file
        text = ""
        for page in doc:
            text += page.get_text() + "\n"
        return text
    else:
        return "No file uploaded."

st.title("📄 PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text:", pdf_text, height=300)
