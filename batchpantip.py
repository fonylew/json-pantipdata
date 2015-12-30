#!/usr/bin/python

import json,sys
import moduleconcat

# get start filename and end filename
start_file = input("start folder number : ")
end_file = input("end folder number : ")

# out = open("comment.csv", 'w')
for folder in range(start_file, end_file+1):
    # create output file named as folder name
    f = open(str(folder), 'w')
    # loop in all files in range
    for n in range(0000,10000):
        # check if that file exists
        try:
            data = json.load(open(str("../pantip-samples/"+str(folder)+"/"+str(folder)+str(n)+".json")))
        except IOError:
            continue
        except ValueError:
            print str(folder)+str(n)
            continue
        # loop in all comments 
        for i in range(len(data["comments"])):
            #print data["user"]["id"] +','+ data["comments"][i]["user"]["id"]
            # print to out file
            f.write(data["user"]["id"] +','+ data["comments"][i]["user"]["id"]+"\n")
            # out.write(data["user"]["id"] +','+ data["comments"][i]["user"]["id"]+"\n")
    f.close()
    print "--"+str(folder)+"--"

moduleconcat.concat(start_file,end_file)
