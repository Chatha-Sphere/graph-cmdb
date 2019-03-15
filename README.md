#### About
Manages CKM IT assets/hardware in a graph database/flask admin API.

#### Instructions
1. To launch the neo4j docker container locally, `make rundb`
2. To enter the container, `docker exec -it curious_george /bin/bash`
3. To run the data import script from inside the container, `cat import/start.cql | NEO4J_USERNAME=neo4j bin/cypher-shell`