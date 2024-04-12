#!/usr/bin/python3
"""
This is the add_integer module
"""


def add_integer(a, b=98):

    """
    Returns the sum of a and b

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int,float)):
        raise TypeError("b must be an integer")
    return(int(a)+int(b))

