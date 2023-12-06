#!/usr/bin/python3
""" Check """
import inspect
from models.rectangle import Rectangle

update_fct = Rectangle.__dict__.get("update")
if update_fct is None:
    print("Rectangle doesn't have method update")
    exit(1)

if not inspect.isfunction(update_fct):
    print("update is not a function")
    exit(1)

print("OK", end="")
