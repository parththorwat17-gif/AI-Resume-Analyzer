import streamlit as st
from google import genai

# Create a client with your API key
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"])

def get_ai_feedback(resume_text, job_role):
    prompt = f"""
Analyze this resume for {job_role}

Resume:
{resume_text}

Provide:

1. Summary
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions
6. ATS Score
"""

    # Call Gemini 2.5 Flash
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
