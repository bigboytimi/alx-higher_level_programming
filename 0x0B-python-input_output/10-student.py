#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """A class called Student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of student
            second_name (str): The second name of student
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get the representation of a dictionary.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if isinstance(attrs, list) and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
