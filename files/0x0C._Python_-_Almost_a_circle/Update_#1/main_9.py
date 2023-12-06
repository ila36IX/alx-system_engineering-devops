#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)
if r.y != 0:
    print("y must be equal to 0: {}".format(r.y))
    exit(1)

r.update(y=1)
    
if r.width != 10:
    print("width must stay to 10: {}".format(r.width))
    exit(1)
    
if r.height != 12:
    print("height must stay to 12: {}".format(r.height))
    exit(1)

if r.x != 0:
    print("x must stay to 0: {}".format(r.x))
    exit(1)

if r.y != 1:
    print("y must be updated to 1: {}".format(r.y))
    exit(1)
    
print("OK", end="")
