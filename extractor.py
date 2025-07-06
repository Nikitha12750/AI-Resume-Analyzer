from pdfminer.high_level import extract_text
from typing import BinaryIO

def extract_pdf_text(pdf_file: BinaryIO) -> str:
    """
    Extracts and returns clean text from a PDF file-like object.
    """
    try:
        # pdf_file is a file-like object (BytesIO or similar)
        text = extract_text(pdf_file)
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {e}" 