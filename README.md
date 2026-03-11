
This repository contains an example script for parsing resumes using the Resume Parser Framework.

## Prerequisites

- Python 3.x
- Required dependencies (install via `pip install -r requirements.txt` if available)
- Example resume files: `examples/example_resume.pdf` and `examples/example_resume.docx`

## Running the Example

1. Ensure you are in the project root directory.
2. Create a .env file and add your own Gemini API key in the following pattern:
   ```GEMINI_API_KEY=<your_key_here>

3. Run the example script:

   ```bash
   python src/example_usage.py

4. The script will parse the example PDF and Word resume files and print the extracted information (name, email, skills) in the console.

## Running the test suite locally
To run the unit tests locally:

1. Ensure you are in the project root directory.
2. Install pytest if not already installed: pip install pytest
3. Run the tests: python -m pytest tst/test_resume_parser.py

This will execute the test suite and display the results in the terminal.