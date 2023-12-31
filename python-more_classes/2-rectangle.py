#!/usr/bin/python3

"""defines the rectangle class"""


class Rectangle:
    """represent a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes a new rectanfle object witj width and height"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set de width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        return self.__width * self.__height
        """Calculate the area of the rectangle."""
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)
