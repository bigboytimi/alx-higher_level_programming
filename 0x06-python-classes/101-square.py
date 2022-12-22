#!/usr/bin/python3
"""Manipulating Class."""


class Square:
    """Make a class called Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Assign values to private attributes.

        Args:
            size(int) = size of the square
            position(int, int) = position of space.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set values for size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set values for position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        result = self.__size ** 2
        return result

    def my_print(self):
        """Print to squares to stdout."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for num in range(0, self.__position[0])]
            [print("#", end="") for char in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
