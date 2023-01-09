#!/usr/bin/python3
"""Returns the list of available attributes and methods of an object"""


def lookup(obj):
    """look up and return obj attributes."""
    result = [i for i in dir(obj)]
    return result
