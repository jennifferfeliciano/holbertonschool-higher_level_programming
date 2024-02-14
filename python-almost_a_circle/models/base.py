#!/usr/bin/python3

"""This module defines the class Base
"""


class Base:
    """
    Class for managing objects with unique id
    """

    __nb_objects = 0
    """
    Class attribute keeping track of a number of created objects
    """

    def __init__(self, id=None):
        """
        Initilizes an instance of the class Base

        Parameters:
        -id: Unique identifier fo the instance

        Attributies:
        -id: Unique identifier of the instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
