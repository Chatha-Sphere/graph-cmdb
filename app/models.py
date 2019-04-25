from py2neo import Graph
from py2neo.ogm import GraphObject, Property
from config import Config
#no support for constraining property type...this should get enforced on the forms?
#how to synchronize forms and models

#unelegant solution to circular imports :(
graph = Graph(bolt = True, host='db', post='7687', 
    user = Config.NEO4J_USER, 
    password=Config.NEO4J_PASSWORD)

class BaseModel(GraphObject):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print("Error: unexpected property")

    @classmethod
    def from_form(cls, form):
        d = form.to_dict()
        for k in ["csrf_token", "submit"]:
            try:
                d.pop(k)
            except KeyError:
                print("Key not found")
        base_model = cls(**d)
        return base_model

    @property
    def all(self):
        return self.select(graph)

    def save(self):
        graph.push(self)

class Asset(BaseModel):
    # __primarykey__ = 'name'

    name = Property()
    asset_type = Property()
    loc = Property()
    desc = Property()
    access = Property()
    admin = Property()
    url = Property()
    #environment / virtual location
    #or model that as a dependency
    #leave it until their is a better definition
    submit = Property()

    #define get/set methods?

class HardwareItem(BaseModel):

    serial_number = Property()
    hardware_type = Property()
    loc = Property()
    assigned_to = Property()
    admin_pw = Property()
    status = Property()
    name = Property()
    submit = Property()

#custom class for relationships?
# class Dependency(Relationship):
# getters/setters?
# yuck
#     pass