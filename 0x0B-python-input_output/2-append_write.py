#!/usr/bin/python3
"""Define a function that appends a string."""


def append_write(filename="", text=""):
    """Returns number of characters added."""
    with open(filename, "a", encoding="utf-8") as new_file:
        new_file.append(text)

        number = new_file.tell()
        return number
