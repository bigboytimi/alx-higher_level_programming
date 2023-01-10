#!/usr/bin/python3
"""Returns an object representation of JSON."""


def from_json_string(my_str):
    """return an object represented by json."""
    return json.loads(my_str)
