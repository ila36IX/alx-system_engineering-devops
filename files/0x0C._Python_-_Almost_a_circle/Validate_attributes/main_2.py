#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

try:
    Rectangle(13, 10, "12")
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "x must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(13, 10, [13])
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "x must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(13, 10, 13.12)
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "x must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Rectangle(13, 10, { 'id': 12 })
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "x must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

print("OK", end="")
