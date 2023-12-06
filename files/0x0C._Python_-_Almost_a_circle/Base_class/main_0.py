#!/usr/bin/python3
""" Check """
import inspect

base_import = __import__('models.base').base

if base_import is None:
    print("Can't import models.base")
    exit(1)

base_class = base_import.__dict__.get('Base')
if base_class is None:
    print("Can't find class Base in models.base")
    exit(1)

if not inspect.isclass(base_class):
    print("Base is not a class")
    exit(1)

print("OK", end="")
