#!/usr/bin/python3
""" Check """
from models.base import Base

list_dictionaries = []
rjson = Base.to_json_string(list_dictionaries)
rjson_expected = "[]"

if rjson is None:
    print("to_json_string is not returning a string")
    exit(1)

if rjson != rjson_expected:
    print("to_json_string on {} must return {}: {}".format(list_dictionaries, rjson_expected, rjson))
    exit(1)

print("OK", end="")
