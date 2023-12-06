#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)

try:
    r.x = -12
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "x must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.x = -89
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "x must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.x = -1
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "x must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    r.x = 0
    print("OK", end="")
except Exception as e:
    print("0 is valid for x: [{}] {}".format(type(e), e))
    exit(1)
