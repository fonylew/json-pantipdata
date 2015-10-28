#!/usr/bin/python

import json,sys
from pprint import pprint

#with open(str(sys.argv[1])) as data_file:
#    data = json.load(data_file)

try:
    folder = input("folder name (can leave blank) : ")
except SyntaxError:
    folder = False

data_file = input("start file number (without .json) : ")
end_file = input("end file number (without .json) : ")

f = open(str(folder), 'w')

#pprint(data)
#pprint(data["comments"])
#print data["user"]["id"]
#print data["user"]["name"]
#print data["emotion"]["likeScore"]
#print data["emotion"]["voters"]#["userId"]

for n in range(data_file,end_file):
    try:
        if not folder:
            data = json.load(open(str("../pantip-samples/"+str(n)+".json")))
        else:
            data = json.load(open(str("../pantip-samples/"+str(folder)+"/"+str(n)+".json")))
    except IOError:
        continue
    for i in range(len(data["comments"])):
        print data["user"]["id"] +','+ data["comments"][i]["user"]["id"]
        f.write(data["user"]["id"] +','+ data["comments"][i]["user"]["id"]+"\n")
        #print len(data["comments"])
f.close()
print "--end--"
