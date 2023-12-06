#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 10)
ra = r.area()
if ra != 100:
    print("Wrong area value: {}".format(ra))
    exit(1)
    
print("OK", end="")
