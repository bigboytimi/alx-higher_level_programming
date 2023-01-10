#!/usr/bin/python3
"""Define a class Square."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a subclass of Rectangle called Square."""
    def __init__(self, size):
        """Instantiate the Square size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
