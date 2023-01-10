#!/usr/bin/python3
"""Defines the function that writes to a string."""


def write_file(filename="", text=""):
    """writes a string to a text file and return
    the number of characters written

    Args:
        filename: file to be written to.
        text(string): string to write into file

    Return:
        Number of characters written
    """

    with open(filename, "w", encoding="utf-8") as new_file:
        return new_file.write(text)
