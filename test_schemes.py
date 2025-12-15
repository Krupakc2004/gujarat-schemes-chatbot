
import os
from dotenv import load_dotenv
import google.generativeai as genai
from chatbot import SchemeAssistant

load_dotenv()

def test_bot():
    bot = SchemeAssistant()
    
    questions = [
        "What is Vahli Dikri Yojana?",
        "ખેડૂતો માટે કઈ યોજનાઓ છે? (What schemes are for farmers?)", 
        "Tell me about Namo Lakshmi Yojana and MYSY in both English and Gujarati"
    ]

    print("--- Testing Scheme Knowledge ---")
    for q in questions:
        print(f"\nUser: {q}")
        response = bot.process_message(q)
        print(f"Bot: {response[:500]}...") # Truncate for readability
    
    print("\n--- End Test ---")

if __name__ == "__main__":
    test_bot()
