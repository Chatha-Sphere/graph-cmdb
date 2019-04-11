import os
from flask import Flask, g, Response, request
from neo4j.v1 import GraphDatabase, basic_auth
#from py2neo import Graph

app = Flask(__name__)

#configuration
NEO4J_URI = "bolt://db:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


#db connect
driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD), encrypted=False)
driver.session()

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
    return 'Hello, World!'

# @app.route("/graph")
# def get_graph():
#     db = get_db()
#     # this should be an actual query
#     query = ""
#     results = db.run(query)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')