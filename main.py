import sys
from pathlib import Path
import os
import pyttsx3,PyPDF2

pdfreader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()

# loop page num, extract text and clear new line breaks
number_of_pages = len(pdfreader.pages)
for page_num in range(number_of_pages):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

# append speech.aiff to path
out = str(Path('speech.aiff').resolve())
print(out)

speaker.save_to_file(clean_text, out)
speaker.runAndWait()

speaker.stop()