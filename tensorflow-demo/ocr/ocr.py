import pytesseract
from PIL import Image


def encode():
    # pytesseract.pytesseract.tesseract_cmd = 'G://Program Files (x86)/Tesseract-OCR/tesseract.exe'
    # text = pytesseract.image_to_string(Image.open('H://python/apps/tensorflow-demo/ocr/words.jpg'), lang='chi_sim')
    text = pytesseract.image_to_string(Image.open('words-chi.jpg'), lang='chi_sim+eng')
    # text = pytesseract.image_to_string(Image.open('ddd.jpg'), lang='chi_sim')
    # text = pytesseract.image_to_string(Image.open('eee.png'))
    print(text)


if __name__ == '__main__':
    encode()
