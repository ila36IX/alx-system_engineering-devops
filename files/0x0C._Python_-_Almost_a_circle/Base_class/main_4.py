#!/usr/bin/python3
""" Check """
from models.base import Base

b = Base()
if b is None:
    print("Can't create Base")
    exit(1)

if b.id != 1:
    print("ID is not equal to 1: {}".format(b.id))
    exit(1)
    
for i in range(2):
    btmp = Base()

btest = Base()
if btest is None:
    print("Can't create Base")
    exit(1)

if btest.id != 4:
    print("ID is not equal to 4 after 3 other creations: {}".format(btest.id))
    exit(1)

print("OK", end="")
