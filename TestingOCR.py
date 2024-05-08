import os
import pytesseract
from PIL import Image
# Initialize Tesseract
pytesseract.pytesseract.tesseract_cmd = "Helmet-Number-Plate-Detection\\Tesseract-OCR\\tesseract.exe"
# Open the image
image = Image.open("Helmet-Number-Plate-Detection\\numberplate.jpg")
text = pytesseract.image_to_string(image)
# print("Text extraction completed!")
if text.strip():
    # print("ssss")
    print(text)
else:
    print("No text found.")

print("Text extraction completed!")