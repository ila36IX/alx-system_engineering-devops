#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)
if r.height != 12:
    print("height must be equal to 12: {}".format(r.height))
    exit(1)

r.update(12, 4, 3)

if r.height != 3:
    print("height must be updated to 3: {}".format(r.height))
    exit(1)
    
print("OK", end="")
