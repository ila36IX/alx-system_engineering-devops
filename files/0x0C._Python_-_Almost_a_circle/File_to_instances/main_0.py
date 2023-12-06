#!/usr/bin/python3
""" Check """
from models.base import Base

load_from_file_fct = Base.__dict__.get("load_from_file")
if load_from_file_fct is None:
    print("Base doesn't have method load_from_file")
    exit(1)

print("OK", end="")
