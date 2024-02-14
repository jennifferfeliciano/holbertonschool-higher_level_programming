#!/usr/bin/python3
"""
Module that contains the rectangle class that inherits from Base
"""
from models.base import Base


class Rectangle(Base):

    """Class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Rectangle class.

        Attributes:
        - width: Width of the rectangle.
        - height: Height of the rectangle.
        - x: X-coordinate of the rectangle (default is 0).
        - y: Y-coordinate of the rectangle (default is 0).
        - id: (Optional) Unique identifier for the instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        self.__y = value
