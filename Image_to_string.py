from PIL import Image
import pytesseract
import json
import re
# from App import image_file
def text_extractor(image_file):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Tesseract-OCR\tesseract.exe'
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text

# text = text_extractor(image_file)
# print(text)