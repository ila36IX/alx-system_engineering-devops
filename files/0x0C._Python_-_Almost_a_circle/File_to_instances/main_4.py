#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle
import os
import json


file_path = "Rectangle.json"
if os.path.exists(file_path):
    os.remove(file_path)

with open(file_path, "w") as file:
    file.write("[]")

res = Rectangle.load_from_file()

if res is None:
    print("load_from_file doesn't return an empty list")
    exit(1)

if len(res) != 0:
    print("load_from_file doesn't return an empty list")
    exit(1)

print("OK", end="")
