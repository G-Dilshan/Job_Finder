from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

gemini_llm = GoogleGenerativeAI(
    model="models/gemini-2.0-flash",
    temperature=0.5,
    )

def llm_define():
    return gemini_llm

