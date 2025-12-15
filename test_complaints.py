
import sys
sys.stdout.reconfigure(encoding='utf-8')
from chatbot import SchemeAssistant

def test_complaints():
    bot = SchemeAssistant()
    questions = [
        "Where can I file a complaint about ration shop?",
        "મારે પાણીની ફરિયાદ કરવી છે (I want to complain about water)",
        "Police complaint number?"
    ]

    print("--- Testing Complaint Guidance ---")
    for q in questions:
        print(f"\nUser: {q}")
        response = bot.process_message(q)
        print(f"Bot: {response}")

if __name__ == "__main__":
    test_complaints()
