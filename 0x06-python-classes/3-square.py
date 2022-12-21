#!/usr/bin/python3
"""Class & Object Manipulation."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Get the size of the square.

        Args:
            size (int): The size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Find the current area of the square."""
        result = self.__size ** 2
        return result
