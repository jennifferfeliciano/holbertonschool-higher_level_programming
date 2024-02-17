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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """to calculate and return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """to print the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Method to override the __str__ method"""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.x, self.y, self.width, self.height)
            )

    def update(self, *args, **kwargs):
        """to update attributes with no-keyword arguments"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
