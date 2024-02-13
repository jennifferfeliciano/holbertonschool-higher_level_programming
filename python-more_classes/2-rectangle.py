#!/usr/bin/python3
class Rectangle:
    """
    Rectangle class represents a geometric rectangle.

    Attributes:
    width: Width of the rectangle.
    height: Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
        - width (int): The width of the rectangle
        - height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width property.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width property.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height property.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height property.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return (self.__width + self.__height) * 2
