#!/usr/bin/python3
"""Define a function that returns Json."""


def to_json_string(my_obj):
    """return a Json representation of an object."""
    conv = json.dumps(my_obj)
    return conv
