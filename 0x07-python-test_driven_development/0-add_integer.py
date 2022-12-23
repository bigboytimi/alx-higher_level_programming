#!/usr/bin/python3
"""Integer addition."""


def add_integer(a, b=98):
    """Returns the addition of two integers

    Floats must converted to Integers

    Exception:
        TypeError: If any of the values are non-integer or non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
