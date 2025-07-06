import re

def clean_text(text: str) -> str:
    """
    Cleans up extracted text by normalizing whitespace and removing unnecessary blank lines.
    """
    # Replace multiple spaces/tabs with a single space
    text = re.sub(r'[ \t]+', ' ', text)
    # Replace multiple newlines with a single newline
    text = re.sub(r'\n+', '\n', text)
    return text.strip() 