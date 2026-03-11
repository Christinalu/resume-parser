import re
from .field_extractor import FieldExtractor

# Regex-based extractor for email addresses. It uses a regular expression to search for and extract the first email address found in the resume text.
# if no email address is found, it returns an empty string. This extractor is designed to be simple and effective for most standard email formats.
class EmailExtractor(FieldExtractor):
    EMAIL_REGEX = re.compile(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')

    def extract(self, text) -> str:
        match = self.EMAIL_REGEX.search(text)
        if match:
            return match.group()
        return ""