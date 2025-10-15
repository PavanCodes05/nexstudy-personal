from pypdf import PdfReader

def read_entire_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() + "\n"  # Add a newline for page separation
        return full_text
    except Exception as e:
        return f"An error occurred: {e}"
