bin/neo4j-shell -path data/graph.db -file /opt/data-copy/index.cypher 
bin/neo4j-shell -path data/graph.db -file /opt/data-copy/import.cypher

chmod -R 777 /opt/data
