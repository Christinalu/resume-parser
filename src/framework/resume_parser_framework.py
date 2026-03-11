from __future__ import annotations

from .parser_helper import get_parser
from .resume_extractor import ResumeExtractor
from ..models.resume_data import ResumeData

class ResumeParserFramework:
    def __init__(self, resume_extractor: ResumeExtractor):
        self.resume_extractor = resume_extractor
    
    # Main method to parse a resume file and extract structured data.
    def parse_resume(self, file_path: str) -> ResumeData:
        # 1. Get the appropriate parser based on file extension
        parser = get_parser(file_path)
        # 2. Use the parser to extract raw text from the resume file
        text = parser.parse(file_path)

        return self.resume_extractor.extract(text)