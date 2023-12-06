#!/usr/bin/python3
""" Check """
from models.base import Base

from_json_string_fct = Base.__dict__.get("from_json_string")
if from_json_string_fct is None:
    print("Base doesn't have method from_json_string")
    exit(1)

print("OK", end="")
