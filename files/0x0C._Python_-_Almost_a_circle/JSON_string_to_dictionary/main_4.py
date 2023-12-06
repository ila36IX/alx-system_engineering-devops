#!/usr/bin/python3
""" Check """
from models.base import Base
import json

list_dicts = [{'id': 12}]
res = Base.from_json_string(json.dumps(list_dicts))

if res is None:
    print("from_json_string doesn't return a list of dictionaries: {}".format(res))
    exit(1)

if type(res) is not list:
    print("from_json_string doesn't return a list of dictionaries: {}".format(res))
    exit(1)

if list_dicts != res:
    print("from_json_string doesn't return a list of dictionaries: {} instead of {}".format(res, list_dicts))
    exit(1)

print("OK", end="")
