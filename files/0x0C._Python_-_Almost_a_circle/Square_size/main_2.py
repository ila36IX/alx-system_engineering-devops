#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(5)

try:
    s.size = "12"
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    s.size = [13]
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    s.size = 13.12
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    s.size = { 'id': 12 }
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "width must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

print("OK", end="")
