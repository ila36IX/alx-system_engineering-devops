#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(2)
sa = s.area()
if sa != 4:
    print("Wrong area: {}".format(sa))
    exit(1)

s = Square(7)
sa = s.area()
if sa != 49:
    print("Wrong area: {}".format(sa))
    exit(1)

s = Square(3, 8, 1)
sa = s.area()
if sa != 9:
    print("Wrong area: {}".format(sa))
    exit(1)

print("OK", end="")
