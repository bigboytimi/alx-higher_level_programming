#!/usr/bin/python3
"""Create a class BaseGeometry"""


class BaseGeometry:
    """A class named BaseGeometry"""
    def __init__(self):
        super().__init__()

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be a greater than 0".format(name))
