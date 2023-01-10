#!/usr/bin/python3
"""Defines a function add_attribute."""


def add_attribute(objname, attrname, val):
    """add a new attribute to an object."""

    if not hasattr(objname, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objname, attrname, val)
