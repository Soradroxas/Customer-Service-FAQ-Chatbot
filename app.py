from flask import Flask, render_template, request, jsonify
import json
import nltk
from nltk.tolkenize import word_tokenize

nltk.download('punkt')

app = Flask(__name__)

with