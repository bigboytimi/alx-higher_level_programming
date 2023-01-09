#!/usr/bin/python3
"""Create a class BaseGeometry"""


class BaseGeometry:
    """A class named BaseGeometry"""
    def __init__(self):
        super().__init__()

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name(str): The name of the parameter
            value(str): The parameter to validate
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
