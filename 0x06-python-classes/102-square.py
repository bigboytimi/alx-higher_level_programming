#!/usr/bin/python3
"""Using getters and setters within a class."""


class Square:
    """A class called Square."""

    def __init__(self, size=0):
        """Method to assign the size of a square.

        Args:
            size(int) = size of a square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: value to assign to the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        result = self.__size**2
        return result

    def __eq__(self, other):
        """Define the == comparision to a square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparision to a square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparision to a square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a square."""
        return self.area() >= other.area()
