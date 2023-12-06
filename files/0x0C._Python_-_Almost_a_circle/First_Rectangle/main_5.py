#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(12, 14, 4, 5, 10)
if r is None:
    print("Can't create Rectangle")
    exit(1)

if r._Rectangle__width != 12:
    print("Wrong private width: {}".format(r._Rectangle__width))
    exit(1)

if r.width != 12:
    print("Wrong width getter: {}".format(r._Rectangle__width))
    exit(1)

r.width = 5

if r._Rectangle__width != 5:
    print("Wrong private width: {}".format(r._Rectangle__width))
    exit(1)

if r.width != 5:
    print("Wrong width getter: {}".format(r._Rectangle__width))
    exit(1)

print("OK", end="")
