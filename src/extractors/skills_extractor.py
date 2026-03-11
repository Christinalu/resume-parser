from __future__ import annotations

import json, os
from .field_extractor import FieldExtractor
from dotenv import load_dotenv
load_dotenv() 

class SkillsExtractor(FieldExtractor):
    def __init__(self):
        try:
            from google import genai
        except ImportError:
            raise ImportError("The GenAI library is required to use the SkillsExtractor. "
                            "Please install it using 'pip install google-generativeai'.")
        
        genmini_api_key = os.getenv("GEMINI_API_KEY")
        if not genmini_api_key:
            self.client = None
            raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
     
        self.client = genai.Client(api_key=genmini_api_key)

    def extract(self, text) -> str:
        if not text.strip():
            return ""
        if not self.client:
            # For offline usage or if the API key is not set, we use simple keyword matching as a fallback.
            return self.simple_keyword_extraction(text)
        
        prompt = (
            "You are an expert resume parser. Extract the candidate's skills from the following resume text.\n"
            "Return a JSON array of skills without any additional text or formatting.\n"
            "Resume Text:\n"
            f"{text}\n"
        )
        
        from google.genai import types
        # ref: https://googleapis.github.io/python-genai/
        try:
            response = self.client.models.generate_content(
                model = "gemini-2.5-flash",
                contents = prompt, 
                config = types.GenerateContentConfig(
                    response_mime_type='application/json',
                    temperature=0.1,
                    max_output_tokens=1000
                )
            )
            content = response.text.strip() if response.text else ""
            
            if not content:
                reason = response.candidates[0].finish_reason
                print(f"Warning: Empty response. Finish Reason: {reason}")
                return []
            
            skills = json.loads(content)
            if isinstance(skills, list):
                return skills

        except json.JSONDecodeError as e:
            print(f"JSON Parsing Error: {e}. Raw content: {content}")
            return []
        except Exception as e:
            print(f"API Error: {e}")
        
        return []
    
    def simple_keyword_extraction(self, text):
        # Extract skills/technologies from text by checking which keywords are present
        # Comparison is case-insensitive, but returned items keep original casing
        keywords = ["Python", "Java", "C++", "SQL", "Machine Learning", "Data Analysis", "AWS", "Docker", "Kubernetes"]
        extracted_skills = [keyword for keyword in keywords if keyword.lower() in text.lower()]
        return extracted_skills