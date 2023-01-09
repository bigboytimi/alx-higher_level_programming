#!/usr/bin/python3
"""Returns the list of available attributes and methods of an object"""

def lookup(obj):
    result = [i for i in dir(obj)]
    return result
