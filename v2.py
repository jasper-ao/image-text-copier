from tkinter import *
import pytesseract.pytesseract
from PIL import ImageGrab
from pyperclip import copy

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import os
path = 'C:\\Users\\owner\\Desktop\\coding\\python\\text copier\\text copier.txt'


class selector:
    def __init__(self):
        self.languages = pytesseract.get_languages()
        
        self.root = Tk()
        self.root.title('Text Copier v2')
        self.root.geometry(f'100x{17*len(self.languages) + 30}')
        self.root.configure(background='lightgray')

        self.lb = Listbox(self.root, selectmode=SINGLE, height=len(self.languages), width=100)
        for lang in self.languages: self.lb.insert(END, lang)
        self.lb.pack()

        Button(self.root, text='Confirm', command=self.confirm).pack(pady=5)

        self.root.mainloop()
    
    def confirm(self):
        self.confirmedLang = self.languages[self.lb.curselection()[0]]
        self.root.destroy()


try:
    imgcb = ImageGrab.grabclipboard()
    if imgcb is None: pytesseract.image_to_string(imgcb, lang='eng')

    gui = selector()
    text = pytesseract.image_to_string(imgcb, lang=gui.confirmedLang) # eng, chi_tra

    copy(text.strip('\n'))
    with open(path, 'w') as file:
        file.write(text)

    os.system(f'notepad {path}')
    
except TypeError as err:
    with open(path, 'w') as file:
        file.write(str(err))

    os.system(f'notepad {path}')
