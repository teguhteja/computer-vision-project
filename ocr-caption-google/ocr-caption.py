from PIL import Image, ImageGrab
import pytesseract
import sys

# Run this command in your terminal
# pip install pyperclip
import pyperclip
"""
This script extracts text from an image using OCR (Optical Character Recognition) with pytesseract.

Usage: python ocr-caption.py <image_path>

Parameters:
    image_path (str): The path to the image file.

Returns:
    None

Example:
    python ocr-caption.py /path/to/image.jpg
"""
image = None
image = Image.open("1.png")
# # Step 2: Use pytesseract to extract text from the image
if(len(sys.argv)!=2):
    # Step 3: Use ImageGrab to grab the image from the clipboard
    image = ImageGrab.grabclipboard()
else :
    # Step 4: Check if the clipboard contains an image
    image.save('clipboard_image.png')
    # Step 3:  Load the image from the file path provided as a command-line argument
    image_path = sys.argv[1]
    image = Image.open(image_path)
    # print("Usage: python ocr-caption.py <image_path>")

# Step 4: Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image, lang='eng')

# Step 5: Print the extracted text
print(extracted_text)

pyperclip.copy(extracted_text)
print("Text copied to clipboard.")