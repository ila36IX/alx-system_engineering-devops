#!/usr/bin/python3
""" Check """
from models.base import Base

b = Base(12)
if b is None:
    print("Can't create Base")
    exit(1)

if b.id != 12:
    print("ID is not the same as the one pass as argument: {}".format(b.id))
    exit(1)
    
print("OK", end="")
