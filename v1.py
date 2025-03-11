import pytesseract.pytesseract
from PIL import ImageGrab
from pyperclip import copy

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

try:
    imgcb = ImageGrab.grabclipboard()
    text = pytesseract.image_to_string(imgcb, lang='eng')
    copy(text.strip('\n'))
    print(text)
except TypeError:
    print('error')
