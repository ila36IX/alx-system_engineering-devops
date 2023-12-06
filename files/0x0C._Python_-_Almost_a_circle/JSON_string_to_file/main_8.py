#!/usr/bin/python3
""" Check """
from models.square import Square
import os
import json


file_path = "Square.json"
if os.path.exists(file_path):
    os.remove(file_path)

list_objs = [Square(1), Square(1, 2), Square(1, 2, 3)]
expected_list = [i.to_dictionary() for i in list_objs]
Square.save_to_file(list_objs)

if not os.path.exists(file_path):
    print("save_to_file doesn't create a file {}".format(file_path))
    exit(1)

with open(file_path, "r") as file:
    list_json = json.load(file)

    if list_json is None:
        print("Can't parse {} file".format(file_path))
        exit(1)
    
    if expected_list != list_json:
        print("Wrong serialization: {} instead of {}".format(list_json, expected_list))
        exit(1)


list_objs = [Square(2), Square(4, 1), Square(7, 3, 4)]
expected_list = [i.to_dictionary() for i in list_objs]
Square.save_to_file(list_objs)

if not os.path.exists(file_path):
    print("save_to_file doesn't create a file {}".format(file_path))
    exit(1)

with open(file_path, "r") as file:
    list_json = json.load(file)

    if list_json is None:
        print("Can't parse {} file".format(file_path))
        exit(1)
    
    if expected_list != list_json:
        print("Wrong serialization: {} instead of {}".format(list_json, expected_list))
        exit(1)

print("OK", end="")
