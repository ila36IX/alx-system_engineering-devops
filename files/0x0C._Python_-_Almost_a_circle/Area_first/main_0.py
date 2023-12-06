#!/usr/bin/python3
""" Check """
import inspect
from models.rectangle import Rectangle

area_fct = Rectangle.__dict__.get("area")
if area_fct is None:
    print("Rectangle doesn't have method area")
    exit(1)

if not inspect.isfunction(area_fct):
    print("area is not a function")
    exit(1)

print("OK", end="")
