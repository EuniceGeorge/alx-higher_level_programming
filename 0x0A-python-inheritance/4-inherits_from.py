#!/usr/bin/python3
""" A function """


def inherits_from(obj, a_class):
    """
    Get the class of the object
    Attributes:
    obj, the object
    a_class, the class of the object
    """
    obj_class = type(obj)

    """
    Check if the object's class is a subclass of the specified class
    """
    if issubclass(obj_class, a_class):
        return True

    """
    Check if any parent class of the object's 
    class is a subclass of the specified class
    """
    for parent_class in obj_class.__bases__:
        if issubclass(parent_class, a_class):
            return True
        # Recursively check parent classes
        if inherits_from(parent_class, a_class):
            return True

    return False
