#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(5)

if s.size != 5:
    print("Size of the Square must be 5: {}".format(s.size))
    exit(1)

if s.width != 5:
    print("Width of the Square must be 5: {}".format(s.width))
    exit(1)

if s.height != 5:
    print("Height of the Square must be 5: {}".format(s.height))
    exit(1)

print("OK", end="")
