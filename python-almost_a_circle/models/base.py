#!/usr/bin/python3

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        else:
            self.id = id
