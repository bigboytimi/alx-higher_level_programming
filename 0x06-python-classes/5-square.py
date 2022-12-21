#!/usr/bin/python3
"""Using getters and setters in Class."""


class Square:
    """Make a class square."""

    def __init__(self, size=0):
        """Initiate an object and assign values.

        Args:
            size(int) = size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Getter/setter for current square size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        result = self.__size**2
        return result

    def my_print(self):
        """Print the square with the # character."""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
