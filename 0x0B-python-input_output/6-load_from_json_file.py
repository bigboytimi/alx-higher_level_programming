#!/usr/bin/python3
"""Defines a function that loads from json."""
import json


def load_from_json_file(filename):
    """Creates an object from a json file."""
    with open(filename, "r") as jsonfile:
        json.loads(filename)
