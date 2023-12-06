#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)
if r.y != 0:
    print("y must be equal to 0: {}".format(r.y))
    exit(1)

r.update(x=2)
    
if r.width != 10:
    print("width must stay to 10: {}".format(r.width))
    exit(1)
    
if r.height != 12:
    print("height must stay to 12: {}".format(r.height))
    exit(1)

if r.x != 2:
    print("x must be updated to 2: {}".format(r.x))
    exit(1)

if r.y != 0:
    print("y must stay to 0: {}".format(r.y))
    exit(1)
    
print("OK", end="")
