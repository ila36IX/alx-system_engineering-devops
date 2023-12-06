#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

try:
    Rectangle(-12, 13)
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
    Rectangle(-89, 13)
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
    Rectangle(0, 13)
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
