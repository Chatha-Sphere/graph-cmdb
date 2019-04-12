import os
from flask import Flask, g, Response, request, jsonify, render_template
from neo4j.v1 import GraphDatabase, basic_auth
#from py2neo import Graph

app = Flask(__name__)

#configuration
NEO4J_URI = "bolt://db:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


#db connection
driver = GraphDatabase.driver(NEO4J_URI, auth=basic_auth(NEO4J_USER, NEO4J_PASSWORD), encrypted=False)

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()
        
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

#sessions and transactions:
# method 1: 
# session.run(query_string)
# method 2:
# with driver.session() as session:
#     tx = session.begin_transaction()
#     do_transaction_runs
#     tx.commit()
# method 3:
# with driver.session() as session:
#     result = session.write_transaction(trans_fn, params)

#will probably stick with method 1 for the time being

@app.route("/api/all_assets")
def all_assets():
    db = get_db()
    query = "match(a:Asset) return a"
    results = db.run(query)
    all_assets = []
    for record in results:
        node = record.value()
        all_assets.append({'id':node['id'], 'name':node['name']})
    #return jsonify({'all_nodes':all_nodes})
    return jsonify(all_assets)

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/admin/create_asset")
def create_asset():
    return render_template('create_asset.html')

@app.route("/admin/create_hardware")
def create_hardware():
    return render_template("create_hardware.html")

@app.route("/admin/create_dependency")
def create_dependency():
    return render_template('create_dependency.html')

# @app.route("/api/create_asset/<id>", methods=['GET', 'POST'])
# def create_asset(id):
#     content = request
#     asset_id = content.get('name')
#     asset_name = content.get('id')

#     db = get_db()
#     db.run("createAssetQuery")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

#print("creating asset {}, id {}".format(content['name'], content['id']))

#with get_db() as session:

#create_asset2/?name=bob&id=1