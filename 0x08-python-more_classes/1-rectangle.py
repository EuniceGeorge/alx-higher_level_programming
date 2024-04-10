#!/usr/bin/python3
"""
This is a module that creates a 'Rectangle' class 
It defines a rectangle by: (based on 0-rectangle.py)
"""

class Rectangle:

    """
    This defines Private instance attribute: width
    It also defines Private instance attribute: height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    elif width < 0:
        raise ValueError("width must be >= 0")
    def width(self):
        self.__width = width
    def width(self, value):
        self.__width = value

    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    elif height < 0:
        raise ValueError("height must be >= 0")
    def height(self):
        self.__height = height
    def height(self, value):
        self.__height = value)

