from src.parsers.pdf_parser import PDFParser
from src.parsers.word_parser import WordParser

PARSER_MAPPING = {
    ".pdf": PDFParser(),
    ".docx": WordParser()
}

# Find the file extension to determine which parser to use, to be extended in the future to support more formats. 
# If the format is unsupported, it raises a ValueError with an appropriate message.
def get_parser(file_path):
    for ext, parser in PARSER_MAPPING.items():
        if file_path.endswith(ext):
            return parser

    raise ValueError(f"Unsupported file format: {file_path}")