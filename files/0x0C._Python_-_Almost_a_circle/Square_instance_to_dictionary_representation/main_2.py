#!/usr/bin/python3
""" Check """
from models.square import Square

r = Square(5)
rd = r.to_dictionary()

if rd is None:
    print("to_dictionary is not returning a dictionary")
    exit(1)

if len(rd.keys()) != 4:
    print("to_dictionary is not returning a dictionary with 5 keys: {}".format(rd.keys()))
    exit(1)

print("OK", end="")
