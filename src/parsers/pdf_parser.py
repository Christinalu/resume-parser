from typing import List
from .file_parser import FileParser

# PDFParser uses the PyMuPDF library to extract text from PDF files. 
# It implements the parse method defined in the FileParser abstract base class, allowing it to read a PDF file and return its content as a string. 
# If PyMuPDF is not installed, it raises an ImportError with instructions on how to install it.
class PDFParser(FileParser):
    def parse(self, file_path: str) -> str:
        try:
            import pymupdf
        except Exception as e:
            raise ImportError("PyMuPDF is required to parse PDF files. " \
            "Please install it using 'pip install PyMuPDF'.") from e

        text = []
        with pymupdf.open(file_path) as doc:
            for page in doc:
                text.append(page.get_text("text"))
        return "\n".join(text)