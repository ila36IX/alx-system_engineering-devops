#!/usr/bin/python3
""" Check """
from models.square import Square
from models.base import Base
import json
import random

list_dictionaries = []
map_dictionaries = {}
for i in range(0, 5):
    s = Square(random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2))
    sd = s.to_dictionary()
    list_dictionaries.append(sd)
    map_dictionaries[s.id] = sd

rjson = Base.to_json_string(list_dictionaries)

if rjson is None:
    print("to_json_string is not returning a string")
    exit(1)

output_list = json.loads(rjson)
for output in output_list:
    id_output = output.get('id')
    if id_output is None:
        break
    dict_output = map_dictionaries.get(id_output)
    if dict_output is None:
        break
    if dict_output != output:
        break
    del map_dictionaries[id_output]

if len(map_dictionaries) != 0:
    print("to_json_string doesn't correctly serialize {}: {}".format(list_dictionaries, rjson))
    exit(1)

print("OK", end="")
