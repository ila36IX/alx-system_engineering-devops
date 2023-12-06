#!/usr/bin/python3
""" Check """
import inspect

rectangle_import = __import__('models.rectangle').rectangle

if rectangle_import is None:
    print("Can't import models.rectangle")
    exit(1)

rectangle_class = rectangle_import.__dict__.get('Rectangle')
if rectangle_class is None:
    print("Can't find class Rectangle in models.rectangle")
    exit(1)

if not inspect.isclass(rectangle_class):
    print("Rectangle is not a class")
    exit(1)

from models.base import Base 

if not issubclass(rectangle_class, Base):
    print("Rectangle is not a subclass of Base")
    exit(1)

print("OK", end="")
