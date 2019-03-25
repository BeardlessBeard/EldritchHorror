#!/usr/bin/env python3
import sys
import json

if(len(sys.argv) != 2):
    print('Usage: python3 JSONconvert.py file')
    exit(0)

myObj = []
contents = []

with open(sys.argv[1], 'r') as file:
    for line in file:
        if not line.strip():
            tmpDict = {}
            for obj in contents:
                obj = obj.split(':')
                val = obj[1].strip()
                try:
                    val = int(val)
                except:
                    pass
                # Get rid of spaces in class name
                key = obj[0].strip().replace(' ', '_')
                # fix items to declare
                tmpDict[key] = val
            myObj.append(tmpDict)
            contents.clear()
            continue
        contents.append(line)

name = sys.argv[1].split('.')
name = name[0]

ofile = name + '.json'
with open (ofile, 'w') as fp:
    json.dump(myObj, fp)
