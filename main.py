import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from PIL import Image

img = Image.open("C:/Users/ADI/Desktop/test.png")
text = pytesseract.image_to_string(img)
print(text)