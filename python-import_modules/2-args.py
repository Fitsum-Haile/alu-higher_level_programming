#!/usr/bin/python3
import sys

number_arguments = len(sys.argv) - 1
if __name__ == "__main__":
    if number_arguments == 0:
        print("0 arguments.")
    elif number_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_arguments))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
