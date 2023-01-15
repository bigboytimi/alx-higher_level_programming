#!/usr/bin/python3
"""Define a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class called Square."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of Square."""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
