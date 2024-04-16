#!/usr/bin/python3
""" A function """


def inherits_from(obj, a_class):
    obj_class = type(obj)
    if issubclass (obj_class, a_class):
        return True
    for parent_class in obj_class.__base__:
        if issubclass(parent_class, a_class):
            return True
        if inherits_from(parent_class, a_class):
            return True
    return False
