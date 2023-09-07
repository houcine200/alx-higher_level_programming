#!/usr/bin/python3
import sys
 
leng = len(sys.argv) - 1
if leng == 0:
    print("{} arguments.".format(leng))
else:
    print("{} arguments:".format(leng))
for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
