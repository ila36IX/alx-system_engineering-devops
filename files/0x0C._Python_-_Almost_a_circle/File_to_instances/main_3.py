#!/usr/bin/python3
""" Check """
from models.square import Square
import os
import json


file_path = "Square.json"
if os.path.exists(file_path):
    os.remove(file_path)

res = Square.load_from_file()

if res is None:
    print("load_from_file doesn't return an empty list when the file doesn't exist")
    exit(1)

if len(res) != 0:
    print("load_from_file doesn't return an empty list when the file doesn't exist")
    exit(1)

print("OK", end="")
