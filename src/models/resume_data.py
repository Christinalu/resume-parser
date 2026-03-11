from dataclasses import dataclass
from typing import List

# This class is a data container for resume information, including the candidate's name, email, and a list of their skills.
@dataclass
class ResumeData:
    name: str
    email: str
    skills: List[str]