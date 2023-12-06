#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(12, 14, 4, 5, 10)
if r is None:
    print("Can't create Rectangle")
    exit(1)

if r._Rectangle__y != 5:
    print("Wrong private y: {}".format(r._Rectangle__y))
    exit(1)

if r.y != 5:
    print("Wrong y getter: {}".format(r._Rectangle__y))
    exit(1)

r.y = 13

if r._Rectangle__y != 13:
    print("Wrong private y: {}".format(r._Rectangle__y))
    exit(1)

if r.y != 13:
    print("Wrong y getter: {}".format(r._Rectangle__y))
    exit(1)

print("OK", end="")
