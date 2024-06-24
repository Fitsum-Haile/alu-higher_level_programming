#!/usr/bin/python3


for i in range(26):
    print("{}".format(chr(122 - i - (32 if i % 2 else 0))), end="")
