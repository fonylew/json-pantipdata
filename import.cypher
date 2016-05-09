USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/user.csv" AS nodeUser
MERGE (u:User { id: toInt(nodeUser.userId) });

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/topic.csv" AS nodeTopic
MERGE (p:Topic { id: toInt(nodeTopic.topicId), timestamp: nodeTopic.timestamp, like: nodeTopic.like, emo: nodeTopic.emo });

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/tag.csv" AS nodeTag
MERGE (t:Tag { name: nodeTag.tagName });

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/room.csv" AS nodeRoom
MERGE (r:Room { name: nodeRoom.roomName });

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/replied.csv"  AS rReplied
MATCH (u:User { id: toInt(rReplied.userId)}),(p:Topic { id: toInt(rReplied.topicId)})
CREATE (u)-[:REPLIED { id: toInt(rReplied.commentId), timestamp: rReplied.timestamp } ]->(p);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/posted.csv"  AS rPosted
MATCH (u:User { id: toInt(rPosted.userId)}),(p:Topic { id: toInt(rPosted.topicId)})
CREATE (u)-[:POSTED]->(p);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/classed.csv"  AS rClassed
MATCH (p:Topic { id: toInt(rClassed.topicId)}),(r:Room { name: rClassed.roomName})
CREATE (p)-[:CLASSED]->(r);

USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM "file:///opt/data-copy/tagged.csv"  AS rTagged
MATCH (p:Topic { id: toInt(rTagged.topicId)}),(t:Tag { name: rTagged.tagName})
CREATE (p)-[:TAGGED]->(t);
