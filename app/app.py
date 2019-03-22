from flask import Flask
from py2neo import authenticate, Graph, Node
from py2neo.packages.httpstream.http import SocketErrors
from neo4j import GraphDatabase

app = Flask(__name__)
app.config['GRAPH_USER'] = 'neo4j'
app.config['GRAPH_PASSWORD'] = ''
app.config['GRAPH_URI'] = 'localhost:7474'
driver = GraphDatabase.driver(app.config['GRAPH_URI'], 
    auth=(app.config['GRAPH_USER'], app.config['GRAPH_PASSWORD'])
    )

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()

@app.route('/')
def index():
    return 'the index'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

@app.route("/graph")
def get_graph():
    db = get_db()
    # this should be an actual query
    query = ""
    results = db.run(query)
    



# if __name__ == '__main__':
#     from flask import Flask
#     app = Flask(__name__)
#     app.config['GRAPH_USER'] = 'neo4j'
#     app.config['GRAPH_PASSWORD'] = 'admin'
#     authenticate(
#         'localhost:7474', app.config['GRAPH_USER'], app.config['GRAPH_PASSWORD']
#     )
#     app.config['GRAPH_DATABASE'] = 'http://localhost:7474/db/data/'
#     graph_indexes = {'Species': Node}
#     flask4j = Neo4j(app, graph_indexes)
#     print (flask4j.gdb.neo4j_version)
#     species_index = flask4j.index['Species']
#     print ('species index:', species_index)
#     flask4j.delete_index('Species')

# authenticate(
#     app.config['GRAPH_URL'], app.config['GRAPH_USER'], 
#     app.config['GRAPH_PASSWORD']
# )
##or just connect to the database directly...?
# app.config['GRAPH_DATABASE'] = 'http://{}/db/data/'.format(app.config['GRAPH_URL'])
# graph = Graph(app.config['GRAPH_DATABASE'])
