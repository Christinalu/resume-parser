import re
from .field_extractor import FieldExtractor

# This extractor is designed to extract the candidate's name from the resume text in a simple and effective manner.
# It first looks for lines that start with "Name:" or "Full Name:" and extracts the name following these prefixes.
# If no such lines are found, it assumes that the first non-empty line in the resume is the candidate's name. If no valid name is found, it returns an empty string.
class NameExtractor(FieldExtractor):
    def extract(self, text) -> str:
        # For cases where the name is prefixed with "Name:" or "Full Name:", we can use a regex to find it.
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            NAME_PATTERN = re.compile(r'^(?:Name|Full Name)[:\s]+(.+)$', re.IGNORECASE)
            match = NAME_PATTERN.match(line)
            if match:
                return match.group(1).strip()
            
        # If no prefixed name is found, we assume the first non-empty line is the candidate's name.
        for line in text.splitlines():
            if line.strip():
                return line.strip()
        
        return ""