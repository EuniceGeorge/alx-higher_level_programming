#!/usr/bin/python3
#0-add_integer.py
def add_integer(a, b=98):

    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b
