#!/usr/bin/python3
"""
Contains the definition of the Rectangle class
"""


class Rectangle:
    """
    Rectangle class represents a geometric rectangle.

    Attributes:
    __width (int): Width of the rectangle.
    __height (int): Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance

        Parameters:
        - width (int): The width of the rectangle
        - height (int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for the width property

        Returns:
        int: The width of the rectangle.
        """
        return self__width

    @width.setter
    def width(self, value):
        """Setter method for the width property.

        Parameters:
        value (int): The new width value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
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

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height property.

        Parameters:
        value (int): The new height value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
