#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(5, 1)
rd = r.to_dictionary()

if rd is None:
    print("to_dictionary is not returning a dictionary")
    exit(1)

if len(rd.keys()) != 5:
    print("to_dictionary is not returning a dictionary with 5 keys: {}".format(rd.keys()))
    exit(1)

print("OK", end="")
