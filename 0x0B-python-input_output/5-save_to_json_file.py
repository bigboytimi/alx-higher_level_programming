#!/usr/bin/python3
"""Defines an object that saves a txt."""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file."""
    with open(filename, "w") as f:
        f.write(json.dump(my_obj)

