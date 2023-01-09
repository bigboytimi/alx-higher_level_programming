#!/usr/bin/python3
"""Define a class that inherits another class."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Create a class that inherits another class."""

    def __init__(self, width, height):
        """Validate values"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
