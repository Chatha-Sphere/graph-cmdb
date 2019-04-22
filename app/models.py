#from py2neo import GraphObject
from neo4j import node, relationship

class Asset(node):
    pass

class HardwareItem(node):
    pass

class Dependency(relationship):
    pass