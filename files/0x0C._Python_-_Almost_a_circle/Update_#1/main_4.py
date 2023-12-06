#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)
if r.x != 0:
    print("x must be equal to 0: {}".format(r.x))
    exit(1)

r.update(id=12, width=4, height=3, x=2)

if r.id != 12:
    print("ID must be updated to 12: {}".format(r.id))
    exit(1)
    
if r.width != 4:
    print("width must be updated to 4: {}".format(r.width))
    exit(1)
    
if r.height != 3:
    print("height must be updated to 3: {}".format(r.height))
    exit(1)

if r.x != 2:
    print("x must be updated to 2: {}".format(r.x))
    exit(1)
    
print("OK", end="")
