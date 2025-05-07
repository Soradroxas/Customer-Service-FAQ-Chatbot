import os

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mySecretKey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/authdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False