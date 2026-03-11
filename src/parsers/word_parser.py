from .file_parser import FileParser

class WordParser(FileParser):
    def parse(self, file_path: str) -> str:
        try:
            import docx
        except Exception as e:
            raise ImportError("python-docx is required to parse Word files. "
            "Please install it using 'pip install python-docx'.") from e
        
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])