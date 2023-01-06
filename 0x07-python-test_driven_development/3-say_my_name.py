#!/usr/bin/python3
"""Write a function that prints."""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first name> <last name>


        Args:
            first_name (str): first name
            last_name (str): last name

        Raises:
            TypeError: if first name or last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
