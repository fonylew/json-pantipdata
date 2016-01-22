library(igraph)


library(visNetwork)
library(RNeo4j)

graph = startGraph("http://localhost:7474/db/data/", username = "neo4j", password = "root")

query =  "
MATCH (p1:User)-[:POSTED]->(:Topic)<-[:REPLIED]-(p2:User)
WHERE p1.name < p2.name
RETURN p1.name AS from, p2.name AS to, COUNT(*) AS weight
order by weight desc
"
edges = cypher(graph,query)

head(edges)
nodes = data.frame(id=unique(c(edges$from, edges$to)))
nodes$label = nodes$id

head(nodes)

ig = graph_from_data_frame(edges, directed=F)
nodes$value = betweenness(ig)
head(nodes)

nodes_json = paste0("\"nodes\":", jsonlite::toJSON(nodes))
edges_json = paste0("\"edges\":", jsonlite::toJSON(edges))
between_json = paste0("{", nodes_json, ",", edges_json, "}")
sink(file = 'betweenness.json')
cat(between_json)
sink()

nodes$value = closeness(ig)
head(nodes)

nodes_json = paste0("\"nodes\":", jsonlite::toJSON(nodes))
edges_json = paste0("\"edges\":", jsonlite::toJSON(edges))
close_json = paste0("{", nodes_json, ",", edges_json, "}")
sink(file = 'closeness.json')
cat(close_json)
sink()