import pyautogui
import pytesseract
from PIL import Image
import time

class OCRReader:
    def __init__(self):
        # Setează calea către Tesseract (modifică dacă e necesar)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def capture_screen(self):
        """Face un screenshot al ecranului unde e deschis PDF-ul."""
        time.sleep(2)  # Așteaptă 2 secunde pentru siguranță
        screenshot = pyautogui.screenshot()
        screenshot.save("data/screen.png")
        return screenshot

    def extract_text_from_image(self, image_path="data/screen.png"):
        """Aplică OCR pe imagine și returnează textul detectat."""
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image, lang="eng")
        return extracted_text

    def detect_fields(self):
        """Face screenshot, extrage textul și returnează lista de câmpuri detectate."""
        self.capture_screen()
        text_detected = self.extract_text_from_image()
        fields = self.process_text(text_detected)
        return fields

    def process_text(self, text):
        """Transformă textul detectat în format ușor de utilizat."""
        lines = text.split("\n")
        fields = [line.strip() for line in lines if line.strip()]
        return fields

if __name__ == "__main__":
    ocr = OCRReader()
    detected_fields = ocr.detect_fields()
    print("Câmpuri detectate:", detected_fields)
