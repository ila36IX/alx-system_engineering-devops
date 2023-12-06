#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(5, 7, 2)
if s.id != 1:
    print("ID must be equal to 1: {}".format(s.id))
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

try:
    Square(5, 7, "12")
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "y must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Square(5, 7, [13])
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "y must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Square(5, 7, 13.12)
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "y must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Square(5, 7, { 'id': 12 })
    print("TypeError exception not raised")
    exit(1)
except TypeError as e:
    if str(e) != "y must be an integer":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Square(5, 7, -12)
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "y must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Square(5, 7, -89)
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "y must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Square(5, 7, -1)
    print("ValueError exception not raised")
    exit(1)
except ValueError as e:
    if str(e) != "y must be >= 0":
        print("Wrong exception message: {}".format(e))
        exit(1)
except Exception as e:
    print("Wrong exception: [{}] {}".format(type(e), e))
    exit(1)

try:
    Square(5, 7, 0)
    print("OK", end="")
except Exception as e:
    print("0 is valid for y: [{}] {}".format(type(e), e))
    exit(1)
