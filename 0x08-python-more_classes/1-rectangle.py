#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiate a new Rectangle Object

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width
            

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be an >= 0")
        self.__width = value


    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height
        

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
