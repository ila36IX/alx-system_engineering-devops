#!/usr/bin/python3
""" Check """
from models.base import Base

create_fct = Base.__dict__.get("create")
if create_fct is None:
    print("Base doesn't have method create")
    exit(1)

print("OK", end="")
