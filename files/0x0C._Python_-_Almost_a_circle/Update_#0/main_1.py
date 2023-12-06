#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)
if r.id != 1:
    print("ID must be equal to 1: {}".format(r.id))
    exit(1)

r.update(12)

if r.id != 12:
    print("ID must be updated to 12: {}".format(r.id))
    exit(1)
    
print("OK", end="")
