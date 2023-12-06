#!/usr/bin/python3
""" Check """
import inspect
from models.rectangle import Rectangle

display_fct = Rectangle.__dict__.get("display")
if display_fct is None:
    print("Rectangle doesn't have method display")
    exit(1)

if not inspect.isfunction(display_fct):
    print("display is not a function")
    exit(1)

print("OK", end="")
