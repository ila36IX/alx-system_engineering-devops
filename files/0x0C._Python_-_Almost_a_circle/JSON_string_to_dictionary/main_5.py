#!/usr/bin/python3
""" Check """
from models.base import Base
from models.rectangle import Rectangle
import json
import random

list_dicts = [Rectangle(random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2)).to_dictionary(), Rectangle(random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2)).to_dictionary()]
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
