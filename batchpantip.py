#!/usr/bin/python
#-*-coding: utf-8 -*-
import json
import sys
import codecs
import moduleconcat

reload(sys)
sys.setdefaultencoding('utf-8')
# get start filename and end filename
start_file = input("start folder number : ")
end_file = input("end folder number : ")
print "hello"
# out = open("comment.csv", 'w')
# -- neo4j schema (csv) --
# -- (Node) --
user = open("user.csv",'w')
topic = open("topic.csv",'w')
tag = open("tag.csv",'w')
room = open("room.csv",'w')
# -- [Relation] --
posted = open("posted.csv",'w')
replied = open("replied.csv",'w')
tagged = open("tagged.csv",'w')
classed = open("classed.csv",'w')
# -- Header --
user.write("userId,degree,betweenness_centrality,closeness_centrality,betweenness,closeness\n")
topic.write("topicId,userId,timestamp,like,emo,room\n")
tag.write("tagName\n")
room.write("roomName\n")
posted.write("userId,topicId\n")
replied.write("userId,topicId,commentId,timestamp\n")
tagged.write("topicId,tagName\n")
classed.write("topicId,roomName\n")

directory = ""

for folder in range(start_file, end_file+1):
    # create output file named as folder name
    # f = open(str(folder), 'w')
    # loop in all files in range
    for n in range(0000,10000):
        # check if that file exists
        try:
            data = json.load(codecs.open(directory+str(folder)+"/"+str(folder)+str(n)+".json",'r','utf-8-sig'))
        except IOError:
            continue
        except ValueError:
            print str(folder)+str(n)
            continue
        if data["status"] == "active":
            # not in comment
            # use set to unique
            if 'user' in data:
                user.write(str(data["user"]["id"])+",0,0,0,0,0\n")
                posted.write(str(data["user"]["id"])+","+str(data["id"])+"\n")
            # loop in all rooms (forums in json file)
            if 'user' in data:
                tmp_forums = ""
                for i in range(len(data["forums"])):
                    tmp_forums += data["forums"][i]+"."
                if len(tmp_forums) > 0:
                    tmp_forums = tmp_forums[:-1]
                else:
                    tmp_forums = "unclassified"
                topic.write(str(data["id"])+","+str(data["user"]["id"])+","+data["timestampISO"]+","+str(data["emotion"]["likeScore"])+","+str(data["emotion"]["emotionScore"])+","+tmp_forums+"\n")
            for i in range(len(data["forums"])):
                room.write(data["forums"][i]+"\n")
                classed.write(str(data["id"])+","+data["forums"][i]+"\n")
            for i in range(len(data["tags"])):
                tag.write(str(data["tags"][i])+"\n")
                tagged.write(str(data["id"])+","+str(data["tags"][i])+"\n")
            # loop in all comments 
            for i in range(len(data["comments"])):
                replied.write(str(data["comments"][i]["user"]["id"])+","+str(data["id"])+","+str(data["comments"][i]["id"])+","+str(data["comments"][i]["timestampISO"])+"\n")
                # print data["user"]["id"] +','+ data["comments"][i]["user"]["id"]
                # print to out file
                # f.write(data["user"]["id"] +','+ data["comments"][i]["user"]["id"]+"\n")
                # out.write(data["user"]["id"] +','+ data["comments"][i]["user"]["id"]+"\n")
    #f.close()
    print "--"+str(folder)+"--"
user.close()
topic.close()
tag.close()
room.close()
posted.close()
replied.close()
tagged.close()
classed.close()
sys.exit(0)
moduleconcat.concat(start_file,end_file)
