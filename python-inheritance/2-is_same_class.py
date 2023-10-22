#!/usr/bin/python3


def is_same_class(obj, a_class):

    """function that verifies if an object
      is an instance of a specific class"""
    if type(obj) is a_class:
        return True
    else:
        return False