from flask import Flask, render_template, request, jsonify
import json
import nltk
from  nltk.tokenize import word_tokenize

app = Flask(__name__)

nltk.download('punkt_tab')

with open('knowledge.json') as f:
    knowledge = json.load(f)

def recognize_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    for item in knowledge:
        for pattern in item['patterns']:
            pattern_tokens = word_tokenize(pattern.lower())
            if set(pattern_tokens).intersection(tokens):
                return item['response']
    return "Sorry, I don't understand your question. Can you rephrase it?"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = recognize_intent(user_input)
    print(f"User: {user_input}")
    print(f"Bot: {response}")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=False)