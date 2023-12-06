#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(5, 1, 4, 3)
s.update(89)

if s.id != 89:
    print("ID of the Square must be updated to 89: {}".format(s.id))
    exit(1)
    
print("OK", end="")
