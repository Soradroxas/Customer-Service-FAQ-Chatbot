from flask import Flask, render_template, request, jsonify
import json
import nltk
from  nltk.tokenize import word_tokenize

nltk.download('punkt')

app = Flask(__name__)

with open('knowledge.json') as f:
    knowledge = json.load(f)

def recognize_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    for item in knowledge:
        for patter in item['patterns']:
            pattern_tokens = word_tokenize(patter.lower())
            if set(pattern_tokens).intersection(tokens):
                return item['intent']
    return "Sorry, I don't understand your question. Can you rephrase it?"