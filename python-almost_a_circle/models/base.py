#!/usr/bin/python3


class Base:
    """represents a base object with an unique id"""
    __nb__objects = 0

    def __init__(self, id=None):
        """initializes the base object"""

        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
