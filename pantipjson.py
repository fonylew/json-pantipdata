#!/usr/bin/python

import json,sys

# get folder name and check if it's empty
try:
    folder = input("folder name (can leave blank) : ")
except SyntaxError:
    folder = False

# get start filename and end filename
# start_file = input("start file number (without .json) : ")
# end_file = input("end file number (without .json) : ")

start_file = 0000
end_file = 9999

# create output file named as folder name
f = open(str(folder), 'w')

# loop in all files in range
for n in range(start_file,end_file+1):
    # check if that file exists
    try:
        if not folder:
            data = json.load(open(str("../pantip-samples/"+str(n)+".json")))
        else:
            data = json.load(open(str("../pantip-samples/"+str(folder)+"/"+str(n)+".json")))
    except IOError:
        continue
    # loop in all comments 
    for i in range(len(data["comments"])):
        print data["user"]["id"] +','+ data["comments"][i]["user"]["id"]
        # print to out file
        f.write(data["user"]["id"] +','+ data["comments"][i]["user"]["id"]+"\n")
f.close()
print "--end--"
