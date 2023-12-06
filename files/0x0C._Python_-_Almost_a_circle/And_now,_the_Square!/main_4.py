#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(5, 7, 2, 89)
if s.id != 89:
    print("ID must be equal to 89: {}".format(s.id))
    exit(1)

if s.width != 5:
    print("Width of the Square must be 5: {}".format(s.width))
    exit(1)

if s.height != 5:
    print("Height of the Square must be 5: {}".format(s.height))
    exit(1)

if s.x != 7:
    print("X of the Square must be 7: {}".format(s.x))
    exit(1)

if s.y != 2:
    print("Y of the Square must be 2: {}".format(s.y))
    exit(1)

print("OK", end="")
