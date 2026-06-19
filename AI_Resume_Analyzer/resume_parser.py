import pdfplumber
from docx import Document
from PIL import Image
import pytesseract

# For Windows
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(uploaded_file):

    file_type = uploaded_file.name.split(".")[-1].lower()

    text = ""

    # PDF
    if file_type == "pdf":

        with pdfplumber.open(uploaded_file) as pdf:

            for page in pdf.pages:
                text += page.extract_text() or ""

    # DOCX
    elif file_type == "docx":

        doc = Document(uploaded_file)

        for para in doc.paragraphs:
            text += para.text + "\n"

    # Images
    elif file_type in ["jpg", "jpeg", "png"]:

        image = Image.open(uploaded_file)

        text = pytesseract.image_to_string(image)

    return text