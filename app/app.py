import os
from flask import Flask, g, Response, request
from neo4j import GraphDatabase, basic_auth

app = Flask(__name__)

#configuration
NEO4J_URI = "bolt://0.0.0.0:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

#db connect
#print(NEO4J_PASSWORD)
driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD))

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()
        
@app.route('/')
def hello_world():
    return 'Hello, Worlc!'

# @app.route("/graph")
# def get_graph():
#     db = get_db()
#     # this should be an actual query
#     query = ""
#     results = db.run(query)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')