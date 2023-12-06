#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

r = Rectangle(10, 12)

try:    
    r.width = "12"
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
    r.width = [13]
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
    r.width = 13.12
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
    r.width = { 'id': 12 }
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
