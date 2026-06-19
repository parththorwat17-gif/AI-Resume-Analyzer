from resume_parser import extract_text
from text_cleaner import clean_text

text = extract_text("resume.pdf")

cleaned = clean_text(text)

print(cleaned)