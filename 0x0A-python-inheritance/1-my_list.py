#!/usr/bin/python3
"""Create a class MyList"""


class MyList(list):
    """a class called 'MyList'"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
