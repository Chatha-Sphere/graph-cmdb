LOAD CSV WITH HEADERS FROM "FILE:///assets.csv" AS csvLine
 CREATE (a:Asset {id: toInteger(csvLine.id), name:csvLine.name});

 LOAD CSV WITH HEADERS FROM "FILE:///hardware.csv" AS csvLine
 MERGE (location: Location {name: csvLine.location})
 CREATE (h:HardwareItem {id: toInteger(csvLine.id), type: csvLine.type})
 CREATE (h)-[:LOCATED_IN]->(location);

 LOAD CSV WITH HEADERS FROM "file:///dependencies.csv" AS csvLine
 MATCH (asset:Asset {id: toInteger(csvLine.assetId)}), (dependency:Asset {id: toInteger(csvLine.dependencyId)})
 CREATE (asset)-[:DEPENDS_ON {type: csvLine.type}]->(dependency);

