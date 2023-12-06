#!/usr/bin/python3
""" Check """
import inspect
from models.base import Base

to_json_string_fct = Base.__dict__.get("to_json_string")
if to_json_string_fct is None:
    print("Base doesn't have method to_json_string")
    exit(1)

if type(to_json_string_fct) is not staticmethod:
    print("to_json_string is not a static method")
    exit(1)

print("OK", end="")
