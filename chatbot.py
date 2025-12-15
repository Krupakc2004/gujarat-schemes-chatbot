import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SchemeAssistant:
    def __init__(self):
        self.model = None
        self.chat = None
        
        try:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                print("Error: GEMINI_API_KEY not found in .env file")
                return

            genai.configure(api_key=api_key)
            
            # System instructions for the AI
            system_instruction = """
            You are an AI-powered assistant specialized ONLY in Gujarat Government schemes and services.
            
            CRITICAL INSTRUCTION: KEEP ANSWERS SHORT, IMPORTANT, AND TO THE POINT.
            - Do NOT write long paragraphs. Use bullet points.
            - MAX 100-150 words per answer.

            STRUCTURE FOR SCHEMES:
            1. **Scheme Name**
            2. **What it is** (1 line)
            3. **Key Benefits** (Max 3 points)
            4. **Eligibility** (Max 2 points)
            5. **How/Where to Apply** (Official Website/Link)

            COMPLAINTS & GRIEVANCES (DIRECT INFO ONLY):
            Provide ONLY the contact details for complaints. Do not explain the process unnecessarily.
            - **CM Office (SWAGAT)**: swagat.gujarat.gov.in
            - **CM Helpline**: Call 1905 or WhatsApp +91 7030930344
            - **Police/Emergency**: 100 or 112
            - **Cyber Crime**: 1930
            - **Ration/Food**: 1967 or 1800-233-5500
            - **Electricity**: 19122
            
            LANGUAGE RULE (STRICT):
            - English input -> English Reply.
            - Gujarati input -> Gujarati Reply.
            - Both requested -> English first, then Gujarati.
            - NO Hinglish/Gujlish.

            OUT-OF-SCOPE:
            If unrelated to Gujarat Govt, say:
            English: "I'm sorry, this is not related to Gujarat Government schemes."
            Gujarati: "માફ કરશો, આ ગુજરાત સરકારની યોજનાઓ સાથે સંબંધિત નથી."
            """
            
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=system_instruction
            )
            self.chat = self.model.start_chat(history=[])
            
        except Exception as e:
            print(f"Error initializing SchemeAssistant: {e}")
            self.model = None

    def process_message(self, message):
        if not self.model:
            return "⚠️ System Error: API Key is missing. Please configure the GEMINI_API_KEY in the .env file."

        try:
            response = self.chat.send_message(message)
            return response.text
        except Exception as e:
            return f"⚠️ Error: Unable to process your request. ({str(e)})"
