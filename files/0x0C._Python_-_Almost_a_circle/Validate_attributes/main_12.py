#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)

try:
    r.width = -12
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "width must be > 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.width = -89
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "width must be > 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.width = 0
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "width must be > 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

print("OK", end="")
