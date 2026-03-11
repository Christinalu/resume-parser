from pathlib import Path
from src.extractors.email_extractor import EmailExtractor
from src.extractors.skills_extractor import SkillsExtractor
from src.extractors.name_extractor import NameExtractor
from src.framework.resume_extractor import ResumeExtractor
from src.framework.resume_parser_framework import ResumeParserFramework

def main():
    extractor = {
        "name": NameExtractor(),
        "email": EmailExtractor(),
        "skills": SkillsExtractor()
    }

    resume_extractor = ResumeExtractor(extractor)
    framework = ResumeParserFramework(resume_extractor)

    current_dir = Path(__file__).parent
    pdf_result = framework.parse_resume(f"{current_dir}/examples/example_resume.pdf")
    word_result = framework.parse_resume(f"{current_dir}/examples/example_resume.docx")
    print(f"\n\n====\nPDF Result: {pdf_result}\n\n====\nWord Result: {word_result}")

if __name__ == "__main__":
    main()