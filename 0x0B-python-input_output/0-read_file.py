#!/usr/bin/python3
"""Defines function that reads text file."""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, "r", encoding="utf-8") as new_file:
        for line in new_file:
            print(line, end="")
