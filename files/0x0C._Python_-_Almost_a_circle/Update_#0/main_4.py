#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)
if r.x != 0:
    print("x must be equal to 0: {}".format(r.x))
    exit(1)

r.update(12, 4, 3, 2)

if r.x != 2:
    print("x must be updated to 2: {}".format(r.x))
    exit(1)
    
print("OK", end="")
