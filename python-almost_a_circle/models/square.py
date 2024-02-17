#!/usr/bin/python3
"""Module that contrains the Square class that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter got size"""
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
