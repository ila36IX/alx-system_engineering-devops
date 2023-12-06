#!/usr/bin/python3
""" Check """
from models.square import Square

input_dict = { 'size': 2 }
new_rect = Square.create(**input_dict)

if new_rect is None:
    print("Square.create doesn't create a new Square")
    exit(1)

if type(new_rect) is not Square:
    print("Square.create doesn't create a new Square: {}".format(new_rect))
    exit(1)

if new_rect.id != input_dict.get('id', 1):
    print("New Square doesn't have the right ID: {}".format(new_rect.id))
    exit(1)

if new_rect.size != input_dict['size']:
    print("New Square doesn't have the right size: {}".format(new_rect.width))
    exit(1)

if new_rect.x != input_dict.get('x', 0):
    print("New Square doesn't have the right x: {}".format(new_rect.x))
    exit(1)

if new_rect.y != input_dict.get('y', 0):
    print("New Square doesn't have the right y: {}".format(new_rect.y))
    exit(1)

print("OK", end="")
