import os

class Config():
    DEBUG = True
    ENV = os.environ.get('FLASK_ENV', 'production')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    NEO4J_URI = "bolt://db:7687"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
