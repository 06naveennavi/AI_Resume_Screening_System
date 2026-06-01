import pdfplumber


def parse_resume_text(pdf_path):
    """Extract clean text from a PDF resume using PDFPlumber."""
    all_text = []

    # Open the PDF file and iterate through the pages
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ''
            all_text.append(page_text)

    # Join all extracted page text into one continuous string
    raw_text = '\n'.join(all_text)
    # Normalize whitespace and remove extra blank lines
    clean_text = ' '.join(raw_text.split())
    return clean_text
