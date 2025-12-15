
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key found: {bool(api_key)}")

if api_key:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello, can you hear me?")
        print("Gemini API Test: SUCCESS")
        print("Response:", response.text)
    except Exception as e:
        print("Gemini API Test: FAILED")
        print("Error:", e)
else:
    print("Gemini API Test: FAILED - Key not found")
