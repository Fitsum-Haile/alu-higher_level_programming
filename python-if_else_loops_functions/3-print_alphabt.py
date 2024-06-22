#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if letter == ord('q') or letter == ord('e'):
        continue
    print("{:s}".format(chr(letter)), end="")
