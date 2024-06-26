#!/usr/bin/python3
import sys


number_arguments = len(sys.argv)
print("{} arguments:".format(number_arguments -1))
for i in range(1, number_arguments):
    print("{}: {}".format(i, sys.argv[i]))
