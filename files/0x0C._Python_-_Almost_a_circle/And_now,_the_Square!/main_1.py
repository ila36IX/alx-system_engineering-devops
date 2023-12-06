#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(5)
if s.id != 1:
    print("ID must be equal to 1: {}".format(s.id))
    exit(1)

if s.width != 5:
    print("Width of the Square must be 5: {}".format(s.width))
    exit(1)

if s.height != 5:
    print("Height of the Square must be 5: {}".format(s.height))
    exit(1)

try:
    Square("12")
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
    Square([13])
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
    Square(13.12)
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
    Square({ 'id': 12 })
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
    Square(-12)
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
    Square(-89)
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
    Square(0)
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
