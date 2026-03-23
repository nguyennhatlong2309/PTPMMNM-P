from pdf2image import convert_from_path
import pytesseract
import pdfplumber
import fitz



def is_scan_pdf(file_path, max_pages=10, threshold=100):
    doc = fitz.open(file_path)
    total_text = 0

    for page in doc[:max_pages]:
        total_text += len(page.get_text().strip())

    return total_text < threshold


def get_text(file_path):
    t = ""
   
    if is_scan_pdf(file_path):
        pages = convert_from_path(file_path)
        for page in pages:
            t += pytesseract.image_to_string(page)
    
    else :
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text :
                    t+= text + "\n"
    
    return t


file_path = "RRTO.pdf"
print(get_text(file_path))