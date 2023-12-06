#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)
if r.y != 0:
    print("y must be equal to 0: {}".format(r.y))
    exit(1)

r.update(12, 4, 3, 2, 1)

if r.y != 1:
    print("y must be updated to 1: {}".format(r.y))
    exit(1)
    
print("OK", end="")
