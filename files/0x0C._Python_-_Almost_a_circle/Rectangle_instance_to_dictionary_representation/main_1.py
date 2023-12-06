#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(5, 1)
rd = r.to_dictionary()

if rd is None:
    print("to_dictionary is not returning a dictionary")
    exit(1)

if type(rd) is not dict:
    print("to_dictionary is not returning a dictionary: {}".format(type(rd)))
    exit(1)

print("OK", end="")
