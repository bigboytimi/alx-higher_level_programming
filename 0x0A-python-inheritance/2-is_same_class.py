#!/usr/bin/python3
"""Confirm instance."""


def is_same_class(obj, a_class):
    """Return True if object is instance of a specified class"""
    if type(obj) == a_class:
        return True
    return False
