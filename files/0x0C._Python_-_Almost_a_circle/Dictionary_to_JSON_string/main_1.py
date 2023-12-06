#!/usr/bin/python3
""" Check """
from models.base import Base

rjson = Base.to_json_string([])

if rjson is None:
    print("to_json_string is not returning a string")
    exit(1)

if type(rjson) is not str:
    print("to_json_string is not returning a string: {}".format(type(rjson)))
    exit(1)

print("OK", end="")
