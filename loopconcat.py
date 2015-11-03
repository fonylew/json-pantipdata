#!/usr/bin/python

import json,sys


# get start filename and end filename
start_file = input("start folder number : ")
end_file = input("end folder number : ")

out = open("concat.csv", 'w')
for folder in range(start_file, end_file+1):
    # create output file named as folder name
    try:
        f = open(str(folder))
    except IOError:
            continue
    out.write(f.read())
    f.close()
out.close()
print "--end--"
