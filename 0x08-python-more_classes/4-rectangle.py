#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Initialize a class Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle object

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Get/set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        result = self.__width * self.__height
        return result

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            result = 2 * (self.__width + self.__height)
            return result

    def __str__(self):
        """print the rectangle with the character ``#``"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """return a string representation of rectangle"""
        return "Rectangle(%s, %s)" % (self.__width, self.__height)
