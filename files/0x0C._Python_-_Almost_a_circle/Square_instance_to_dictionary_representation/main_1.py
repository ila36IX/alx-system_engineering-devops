#!/usr/bin/python3
""" Check """
from models.square import Square

r = Square(5)
rd = r.to_dictionary()

if rd is None:
    print("to_dictionary is not returning a dictionary")
    exit(1)

if type(rd) is not dict:
    print("to_dictionary is not returning a dictionary: {}".format(type(rd)))
    exit(1)

print("OK", end="")
