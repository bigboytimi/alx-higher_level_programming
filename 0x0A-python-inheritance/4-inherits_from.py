#!/usr/bin/python3
"""Defines a class-checking function"""


def inherits_from(obj, a_class):
    """return True if obj is an inheritance of a class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
