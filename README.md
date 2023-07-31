A speech to text generator from PDF files.

## Libraries

- [pyttsx3](https://pypi.org/project/pyttsx3/) - Based of NSSpeechSynthesizer (macOS 10.3–14.0 - Deprecated)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation via MacOS 10.10 and above

After installing **pyttsx3** refer to [pull request 35](https://github.com/RapidWareTech/pyttsx/pull/35) and implement [these code changes](https://github.com/RapidWareTech/pyttsx/pull/35/commits/d01b641f3ecc029dde51f74810ea73c9ab0888b8) to enable pyttsx3 to work correctly.

## Instructions

1. Add 'book.pdf' to folder.
2. Run main.py

**Expected Result:**
An aiff file is generated from the text of the PDF.

**Other notes:**
'book.pdf' and 'speech.aiff' can be renamed, when renaming these keep the file extensions.
# pdf2speech
