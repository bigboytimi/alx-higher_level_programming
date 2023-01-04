#!usr/bin/python3

class LockedClass:
    """Prevent users from dynamically creating new instance
    attributes, except if the new instance attribute is called
    'first_name'
    """

    __slots__ = ["first_name"]
