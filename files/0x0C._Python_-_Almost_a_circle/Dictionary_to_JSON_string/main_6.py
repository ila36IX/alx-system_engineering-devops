#!/usr/bin/python3
""" Check """
from models.base import Base
import json
import uuid

list_dictionaries = []
map_dictionaries = {}
for i in range(0, 5):
    rd = { 'id': len(list_dictionaries), 'name': str(uuid.uuid4()) }
    list_dictionaries.append(rd)
    map_dictionaries[rd.get('id')] = rd

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
