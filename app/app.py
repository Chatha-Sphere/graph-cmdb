import os
from config import Config
from flask import Flask, g, Response, request, jsonify, render_template, abort, flash, redirect, url_for
from neo4j import GraphDatabase, basic_auth
from forms import AssetForm, HardwareForm, DependencyForm
#from py2neo import Graph

app = Flask(__name__)
app.config.from_object(Config)

#db connection
driver = GraphDatabase.driver(app.config['NEO4J_URI'], 
    auth=basic_auth(app.config['NEO4J_USER'], app.config['NEO4J_PASSWORD']), 
    encrypted=False)
#db = Graph(bolt = True, host='db', post='7687', user = NEO4J_USER, password=NEO4J_PASSWORD)

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

# @app.route("/api/all_assets")
# #this is broken now :(
# def all_assets():
#     db = get_db()
#     query = "match(a:Asset) return a"
#     results = db.run(query)
#     all_assets = []
#     for record in results:
#         node = record.value()
#         all_assets.append({'id':node['id'], 'name':node['name']})
#     #return jsonify({'all_nodes':all_nodes})
#     return jsonify(all_assets)

@app.route("/admin")
def admin():
    return render_template('admin.html')


#how about abstracting these three views into one function?
#show successful submission
#allow user to add multiple guys in one sitting

@app.route("/admin/create_<entity>", methods=["GET", "POST"])
def create_entity(entity):
    entity_dict = {'asset': ("Asset", AssetForm), 'hardware': ("Hardware Item", HardwareForm), 'dependency': ("Dependency", DependencyForm)}
    if entity_dict.get(entity) is None:
        abort(404)
    name = entity_dict[entity][0]
    form = entity_dict[entity][1]()
    if form.validate_on_submit():
        print(request)
        flash("New {} added!".format(name.lower()), 'success')
        return redirect(url_for('admin'))
    else:
        flash("Error! Input could not be validated", 'error')
    return render_template('create_form.html', entity=entity, entity_name=name, form=form)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

#print("creating asset {}, id {}".format(content['name'], content['id']))

#with get_db() as session:

#create_asset2/?name=bob&id=1