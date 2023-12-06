#!/usr/bin/python3
""" Check """
import inspect
from models.rectangle import Rectangle

to_dictionary_fct = Rectangle.__dict__.get("to_dictionary")
if to_dictionary_fct is None:
    print("Rectangle doesn't have method to_dictionary")
    exit(1)

if not inspect.isfunction(to_dictionary_fct):
    print("to_dictionary is not a function")
    exit(1)

print("OK", end="")
