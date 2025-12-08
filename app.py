from flask import Flask, render_template, request, jsonify
from chatbot import SchemeAssistant

app = Flask(__name__)

# Store chatbot instances for each user session
chat_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_id = request.remote_addr
    user_message = request.json.get('message')
    
    if user_id not in chat_sessions:
        chat_sessions[user_id] = SchemeAssistant()
    
    bot = chat_sessions[user_id]
    response = bot.process_message(user_message)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
