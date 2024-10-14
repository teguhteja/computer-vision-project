import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import argparse
import pyperclip

# Set up argument parser
parser = argparse.ArgumentParser(description='Extract text from a PDF using OCR.')
parser.add_argument('pdf_path', type=str, help='Path to the PDF file')

# Parse arguments
args = parser.parse_args()

# Open the PDF
document = fitz.open(args.pdf_path)

# Loop through each page
extracted_text = ""
for page_number in range(len(document)):
    page = document.load_page(page_number)  # Load page
    pix = page.get_pixmap()  # Render page to an image
    img = Image.open(io.BytesIO(pix.tobytes()))  # Convert to PIL image
    
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    extracted_text += text + "\n"
    print(f"Text from page {page_number + 1}:\n{text}\n")

pyperclip.copy(extracted_text)
document.close()
