library(igraph)
library(visNetwork)
library(RNeo4j)

graph = startGraph("http://localhost:7474/db/data/", username = "neo4j", password = "root")
query =  "MATCH (u1:User)-[:REPLIED]->()"