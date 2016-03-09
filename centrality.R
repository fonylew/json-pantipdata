library(igraph)
library(visNetwork)
library(RNeo4j)

neo4j = startGraph("http://localhost:7474/db/data/", username = "neo4j", password = "root")
browse(neo4j)

query =  "
MATCH (p1:User)-[:POSTED]->(:Topic)<-[:REPLIED]-(p2:User)
WHERE p1.name < p2.name
RETURN p1.name AS source, p2.name AS target, COUNT(*) AS weight
order by weight desc
limit 100
"
edges = cypher(neo4j,query)

head(edges)
nodes = data.frame(id=unique(c(edges$source, edges$target)))
nodes$label = nodes$id

head(nodes)

ig = graph_from_data_frame(edges, directed=F)
nodes$value = betweenness(ig)
head(nodes)

nodes_json = paste0("\"nodes\":", jsonlite::toJSON(nodes))
edges_json = paste0("\"edges\":", jsonlite::toJSON(edges))
between_json = paste0("{", nodes_json, ",", edges_json, "}")
sink(file = 'betweenness_limit100.json')
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

ig = graph.data.frame(edges, directed = FALSE, nodes)
communities = edge.betweenness.community(ig)
memb = data.frame(name = communities$names, cluster = communities$membership)
nodes = merge(nodes, memb)
nodes = nodes[c("id", "name", "cluster")]
