#!/usr/bin/python3
"""write a function that prints a square."""

def print_square(size):
    """print a square.
    
    Args:
        size(int): length of the square.

    Raises:
        TypeError: if size is not an integer or float
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("{}".format(size * "#", end=""))
