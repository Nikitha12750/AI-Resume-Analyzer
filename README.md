# 🧠 AI Resume Analyzer

A simple yet powerful AI-powered web application that allows users to upload their resumes in PDF format and get:
- 🔍 **Resume text extraction**
- 📊 **Scoring based on keyword presence and structure**
- 📝 **Feedback on missing elements**

This project uses **Streamlit** for the frontend and **Python** NLP tools for backend scoring.

---

## 🚀 Features

- Upload resume in PDF format
- Extracts and displays resume content
- Scores based on:
  - Presence of Skills, Education, Projects sections
  - Usage of technical keywords (e.g., Python, JavaScript)
  - Links to GitHub/LinkedIn
  - Grammar/spelling issues
- Gives feedback and tips for improving the resume

---

## 🧱 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python (pdfminer, language_tool_python)
- **Model Logic:** Rule-based scoring

---

## 🗂️ Project Structure

```
├── main.py                # Streamlit frontend
├── resume_parser.py       # Extracts text from PDF
├── resume_scorer.py       # Logic for scoring and feedback
├── utils.py               # Helpers (e.g., keyword check)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## 📦 Installation

```bash
# Clone the repo
https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Run the App

```bash
streamlit run main.py
```
Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ✅ Sample Scoring Criteria

| Feature                              | Points |
|--------------------------------------|--------|
| Skills section present               | +10    |
| Tech keywords (Python, JS, etc.)     | +15    |
| GitHub/LinkedIn present              | +10    |
| Projects/Education section           | +20    |
| Proper grammar/spelling              | +10    |
| Missing key elements                 | -10    |

---

