#!/usr/bin/python3
""" Check """
from models.base import Base

save_to_file_csv_fct = Base.__dict__.get("save_to_file_csv")
if save_to_file_csv_fct is None:
    print("Base doesn't have method save_to_file_csv")
    exit(1)

print("OK", end="")
