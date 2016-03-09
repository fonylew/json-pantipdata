docker pull sequenceiq/hadoop-docker:2.4.1
docker pull kbastani/docker-neo4j:2.2.1
docker pull kbastani/neo4j-graph-analytics:latest

# Create HDFS
docker run -i -t --name hdfs sequenceiq/hadoop-docker:2.4.1 /etc/bootstrap.sh -bash

# Create Mazerunner Apache Spark Service
docker run -i -t --name mazerunner --link hdfs:hdfs kbastani/neo4j-graph-analytics:latest

# Create Neo4j database with links to HDFS and Mazerunner
# Replace <user> and <neo4j-path>
# with the location to your existing Neo4j database store directory
docker run -it -p 7474:7474 -v /Users/handf/Dropbox/CPCU/data:/opt/data-copy --name graphdb --link mazerunner:mazerunner --link hdfs:hdfs kbastani/docker-neo4j:2.2.1 /bin/bash

##################
# P'Nott Command #
##################

#Run Hadoop
docker run -i -t --name hdfs sequenceiq/hadoop-docker:2.4.1 /etc/bootstrap.sh -bash

#Run and Start Mazerunner service
docker run -i -t --name mazerunner --link hdfs:hdfs kbastani/neo4j-graph-analytics:latest 

#Run Neo4j
docker run -ti -p 7474:7474 -v /Users/ponthaiklinsompus/Documents/Neo4j:/opt/data-copy --name graphdb --link mazerunner:mazerunner --link hdfs:hdfs kbastani/docker-neo4j:2.2.1 /bin/bash

#Copy graph.db to /opt/data
cp -r /opt/data-copy/cineasts_12k_movies_50k_actors.db /opt/data
mv /opt/data/cineasts_12k_movies_50k_actors.db /opt/data/graph.db
ls -l /opt/data/

#Start Neo4j
bin/neo4j start


##################
#  spark-neo4j   #
##################

docker run -ti --name neospark  kbastani/spark-neo4j up -d /bin/bash

