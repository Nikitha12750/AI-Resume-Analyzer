# Streamlit PDF Resume Text Extractor

This app lets you upload a PDF resume, extracts clean text using `pdfminer.six`, and displays it in the browser using Streamlit.

## Features
- Upload a PDF resume
- Extracts and cleans text from the PDF
- Displays the extracted text in a user-friendly interface

## Setup
1. **Clone the repository or download the project files.**
2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `app.py` - Main Streamlit app
- `extractor.py` - PDF text extraction logic
- `utils.py` - Utility functions (e.g., text cleaning)

## Notes
- Only PDF files are supported.
- Extraction quality depends on the PDF's formatting. 