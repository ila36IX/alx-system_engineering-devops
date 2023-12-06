#!/usr/bin/python3
""" Check """
import inspect

square_import = __import__('models.square').square

if square_import is None:
    print("Can't import models.square")
    exit(1)

square_class = square_import.__dict__.get('Square')
if square_class is None:
    print("Can't find class Square in models.square")
    exit(1)

if not inspect.isclass(square_class):
    print("Square is not a class")
    exit(1)

from models.rectangle import Rectangle

if not issubclass(square_class, Rectangle):
    print("Square is not a subclass of Rectangle")
    exit(1)

print("OK", end="")
