#! /usr/bin/env bash

echo "Importing test data into Neo4j"
echo "$PWD"
cat import/start.cql | NEO4J_USERNAME=neo4j bin/cypher-shell