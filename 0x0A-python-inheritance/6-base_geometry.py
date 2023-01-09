#!/usr/bin/python3
"""Create a class BaseGeometry"""


class BaseGeometry:
    """A class named BaseGeometry"""
    def __init__(self):
        super().__init__()

    def area(self):
        raise Exception("area() is not implemented")
