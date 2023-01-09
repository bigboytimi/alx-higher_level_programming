#!/usr/bin/python3
"""Check if obj is an instance of class or subclass"""


def is_kind_of_class(obj, a_class):
    """Return True if it is an instance, return false if not"""
    if isinstance(obj, a_class):
        return True
    return False
