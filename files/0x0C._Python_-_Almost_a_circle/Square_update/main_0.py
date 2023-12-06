#!/usr/bin/python3
""" Check """
import inspect
from models.square import Square

update_fct = Square.__dict__.get("update")
if update_fct is None:
    print("Square doesn't have method update")
    exit(1)

if not inspect.isfunction(update_fct):
    print("update is not a function")
    exit(1)

print("OK", end="")
