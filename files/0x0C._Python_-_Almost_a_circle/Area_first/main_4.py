#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12, 1, 3)
ra = r.area()
if ra != 120:
    print("Wrong area value: {}".format(ra))
    exit(1)
    
print("OK", end="")
