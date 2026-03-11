import pytest

from src.extractors.name_extractor import NameExtractor
from src.extractors.skills_extractor import SkillsExtractor
from src.extractors.email_extractor import EmailExtractor
from src.framework.resume_extractor import ResumeExtractor
from src.framework.parser_helper import get_parser
from src.framework.resume_parser_framework import ResumeParserFramework

SAMPLE_TEXT = """
Alex Rivers

Full Stack Developer | alex.rivers@email.com | +1-555-0123 | GitHub: github.com/arivers | alex.river@fakedomain.com

Summary
Versatile Full Stack Developer with 5 years of experience building scalable web applications. Expert in React, Node.js, and cloud architecture.

Technical Skills
Languages: JavaScript, TypeScript, Python, SQL
Frontend: React, Redux, Tailwind CSS, Next.js
Backend: Node.js, Express, PostgreSQL, MongoDB
Tools: Docker, AWS, Git, CI/CD
"""

def test_name_extractor():
    extractor = NameExtractor()
    assert extractor.extract(SAMPLE_TEXT) == "Alex Rivers"

def test_email_extractor():
    extractor = EmailExtractor()
    assert extractor.extract(SAMPLE_TEXT) == "alex.rivers@email.com"

def test_skills_extractor():
    extractor = SkillsExtractor()
    skills = extractor.extract(SAMPLE_TEXT)
    assert "JavaScript" in skills
    assert "React" in skills
    assert "Node.js" in skills
    assert "AWS" in skills

def test_resume_extractor():
    field_extractors = {
        "name": NameExtractor(),
        "email": EmailExtractor(),
        "skills": SkillsExtractor()
    }
    resume_extractor = ResumeExtractor(field_extractors)
    resume_data = resume_extractor.extract(SAMPLE_TEXT)
    
    assert resume_data.name == "Alex Rivers"
    assert resume_data.email == "alex.rivers@email.com"
    assert "JavaScript" in resume_data.skills
    assert "Git" in resume_data.skills
    assert "PostgreSQL" in resume_data.skills
    assert "CI/CD" in resume_data.skills

def test_framework_parser_with_text():
    field_extractors = {
        "name": NameExtractor(),
        "email": EmailExtractor(),
        "skills": SkillsExtractor()
    }
    resume_extractor = ResumeExtractor(field_extractors)
    framework = ResumeParserFramework(resume_extractor)

    # Test with sample text directly
    with pytest.raises(ValueError):
        framework.parse_resume(SAMPLE_TEXT)

def test_parser_helper():
    # Test PDF parser
    pdf_parser = get_parser("sample_resume.pdf")
    assert pdf_parser is not None
    assert hasattr(pdf_parser, "parse")

    # Test Word parser
    word_parser = get_parser("sample_resume.docx")
    assert word_parser is not None
    assert hasattr(word_parser, "parse")

    # Test unsupported format
    with pytest.raises(ValueError):
        get_parser("sample_resume.txt")