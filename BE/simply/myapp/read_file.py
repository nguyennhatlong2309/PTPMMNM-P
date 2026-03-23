from pdf2image import convert_from_path
import pytesseract
import fitz
from concurrent.futures import ThreadPoolExecutor

file_path = "../RRTO.pdf"

def is_scan_pdf(file_path, max_pages=5, threshold=100):
    doc = fitz.open(file_path)
    total_text = 0
    for page in doc[:max_pages]:
        total_text += len(page.get_text().strip())
    return total_text < threshold

def ocr_page(page): 
    # chuyển ảnh thành chuỗi
    return pytesseract.image_to_string(page)

def ocr_pages_multithread(pages, max_workers=20):
    text = ""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(ocr_page, pages)
        for page_text in results:
            text += page_text
    return text

def get_text(file_path, max_pages_for_scan_check=5, dpi=150, max_workers=20):
    t = ""
    if is_scan_pdf(file_path, max_pages=max_pages_for_scan_check):
        pages = convert_from_path(file_path, dpi=dpi)
        t = ocr_pages_multithread(pages, max_workers=max_workers)
    else:
        doc = fitz.open(file_path)
        for page in doc:
            text = page.get_text()
            if text:
                t += text + "\n"
    return t
