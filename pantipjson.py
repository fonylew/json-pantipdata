import json,sys
from pprint import pprint

with open(str(sys.argv[1])) as data_file:
    data = json.load(data_file)

#pprint(data)
#pprint(data["comments"])
#print data["user"]["id"]
#print data["user"]["name"]
#print data["emotion"]["likeScore"]
#print data["emotion"]["voters"]#["userId"]
for i in range(len(data["comments"])):
    print data["user"]["id"] +','+ data["comments"][i]["user"]["id"]
#print len(data["comments"])

