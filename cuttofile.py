#!/usr/bin/python
#-*-coding: utf-8 -*-
import json
import sys
import os
import codecs

reload(sys)
sys.setdefaultencoding('utf-8')
# get start filename and end filename
start_file = input("start folder number : ")
end_file = input("end folder number : ")
print "...starting..."

for folder in range(start_file, end_file+1):
    if not os.path.exists(str(folder)):
        os.makedirs(str(folder))
        print "create new folder "+str(folder)
    with open("data-"+str(folder)+".json") as f:
        for line in f:
            id = line[6:14]
            topic = open(str(folder)+"/"+id+".json",'w')
            topic.write(line)
            topic.close()
    f.close()
    print "--"+str(folder)+"--"
print "...finish..."
sys.exit(0)
