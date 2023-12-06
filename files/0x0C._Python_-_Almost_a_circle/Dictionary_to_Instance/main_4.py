#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle

input_dict = { 'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89 }
new_rect = Rectangle.create(**input_dict)

if new_rect is None:
    print("Rectangle.create doesn't create a new Rectangle")
    exit(1)

if type(new_rect) is not Rectangle:
    print("Rectangle.create doesn't create a new Rectangle: {}".format(new_rect))
    exit(1)

if new_rect.id != input_dict.get('id', 1):
    print("New Rectangle doesn't have the right ID: {}".format(new_rect.id))
    exit(1)

if new_rect.width != input_dict['width']:
    print("New Rectangle doesn't have the right width: {}".format(new_rect.width))
    exit(1)

if new_rect.height != input_dict['height']:
    print("New Rectangle doesn't have the right height: {}".format(new_rect.height))
    exit(1)

if new_rect.x != input_dict.get('x', 0):
    print("New Rectangle doesn't have the right x: {}".format(new_rect.x))
    exit(1)

if new_rect.y != input_dict.get('y', 0):
    print("New Rectangle doesn't have the right y: {}".format(new_rect.y))
    exit(1)

print("OK", end="")
