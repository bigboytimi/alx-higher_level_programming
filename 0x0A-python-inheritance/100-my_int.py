#!/usr/bin/python3
"""Define a class MyInt."""

class MyInt(int):
    """A class called MyInt"""

    def __eq__(self, value):
        """Overrides the equality operator with negative."""
        return self.real != value

    def __ne__(self, value):
        """Overrides the negative operator with equality."""
        return self.real == value

