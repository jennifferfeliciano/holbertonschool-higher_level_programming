#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """function that verifies if the object is an instance of,
    or if the object is an instance of a
    class that inherited from, the specified class"""

    return issubclass(type(obj), a_class)