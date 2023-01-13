#!/usr/bin/python3
"""Write class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """A class called Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout."""


        ht = self.__height
        wt = self.__width
        [print("") for y in range(self.y)]
        for i in range(ht):
            [print(" ", end="") for x in range(self.x)]
            for j in range(wt):
                print("#", end="")
            print("")

    def __str__(self):
        """return method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, 
                                                self.x, self.y, 
                                                self.width, self.height)
