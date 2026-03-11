from __future__ import annotations
from ..models.resume_data import ResumeData
from ..extractors.field_extractor import FieldExtractor

# Orchestrate fields extraction from resume text to build a ResumeData object.
class ResumeExtractor:
    def __init__(self, field_extractors: dict[str, FieldExtractor]):
        self.field_extractors = field_extractors

    def extract(self, resume_text: str) -> ResumeData:
        name = self.field_extractors["name"].extract(resume_text)
        email = self.field_extractors["email"].extract(resume_text)
        skills = self.field_extractors["skills"].extract(resume_text)
        return ResumeData(name=name, email=email, skills=skills)