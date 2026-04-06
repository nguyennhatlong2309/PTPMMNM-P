from pdf2image import convert_from_bytes
import pytesseract
import fitz
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import io
import docx
import time
# ================= PDF =================
def is_scan_pdf(doc, max_pages=5, threshold=100):
    total_text = 0
    for page in doc[:max_pages]:
        total_text += len(page.get_text().strip())
    return total_text < threshold

def ocr_page(page): 
    return pytesseract.image_to_string(page)

def ocr_pages_multithread(pages, max_workers=8):
    text = ""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(ocr_page, pages)
        for page_text in results:
            text += page_text
    return text

def read_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")

    if is_scan_pdf(doc):
        pages = convert_from_bytes(file_bytes, dpi=150)
        return ocr_pages_multithread(pages)
    else:
        text = ""
        for page in doc:
            t = page.get_text()
            if t:
                text += t + "\n"
        return text

# ================= IMAGE =================
def read_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes))
    return pytesseract.image_to_string(image)

# ================= DOCX =================
def read_docx(file_bytes):
    doc = docx.Document(io.BytesIO(file_bytes))
    text = "\n".join([p.text for p in doc.paragraphs])
    return text

# ================= MAIN =================
def get_text(file_bytes, filename):
    filename = filename.lower()

    if filename.endswith(".pdf"):
        return read_pdf(file_bytes)

    elif filename.endswith((".png", ".jpg", ".jpeg")):
        return read_image(file_bytes)

    elif filename.endswith(".docx"):
        return read_docx(file_bytes)

    else:
        return "Unsupported file type"


