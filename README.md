#### About
Helps administer CKM IT assets and hardware in a Flask API built on a Neo4j database.

#### Schema Design (WIP)
ADMIN PANEL
1.  Create new: assets, hardware items, dependencies
2.  Update/delete (incl. search bar)

USER VIEW
1. Table views of entitys, incl. assets by environment (e.g Rancher) and hardware by type (e.g. MacBooks)
2. Graph views of entities
    * Select an asset and see related items
    * Cause-and-effect: what items would be affected by changes to an asset's property?


