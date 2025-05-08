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
        for pattern in item['patterns']: