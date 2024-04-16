#!/usr/bin/python3
""" A function that returns true"""


def is_same_class(obj, a_class):
    """ A function that has two argments obj and a_class
    Check if the object's class is exactly the same as the specified class
    """
    obj_class = type(obj)
    if obj_class == a_class:
        return True
    else:
        return False
