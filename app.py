import streamlit as st
from extractor import extract_pdf_text
from utils import clean_text
from io import BytesIO

st.title("PDF Resume Text Extractor")
st.write("Upload your PDF resume to extract and view the clean text.")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Read the uploaded file as a BytesIO object
    pdf_bytes = BytesIO(uploaded_file.read())
    with st.spinner("Extracting text from PDF..."):
        raw_text = extract_pdf_text(pdf_bytes)
        cleaned_text = clean_text(raw_text)
    st.subheader("Extracted Text:")
    st.text_area("", cleaned_text, height=400) 