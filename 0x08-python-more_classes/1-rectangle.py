#!/usr/bin/python3
"""
This is a module that creates a 'Rectangle' class 
It defines a rectangle by: (based on 0-rectangle.py)
"""

class Rectangle:

    """
    The Rectangle Class:
    This defines Private instance attribute: width
    It also defines Private instance attribute: height
    Has two internal properties, and two methods to change them.
    Optional arguments specify the width and height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int) or not isinstance(height, int):
            wrong = 'width' if not isinstance(width, int) else 'height'
            raise TypeError( wrong  + "must be an integer")
        if width < 0 or height < 0:
            wrong = 'width' if width < 0 else 'height'
            raise ValueError(wrong + "must be >= 0")
        self.__width = width
        self.__height = height

        @property
        def width(self):
            return(self.__width)

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

        @property
        def height(self):
            return(self.__height)

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value

