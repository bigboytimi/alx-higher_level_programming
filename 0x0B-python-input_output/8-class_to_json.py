#!/usr/bin/python3
"""Define a function class_to_json."""


def class_to_json(obj):
    """Returns the dictionary representation of object."""
    return obj.__dict__
