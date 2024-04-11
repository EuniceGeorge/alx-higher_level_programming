#!/usr/bin/python3
"""
The Rectangle Module:
"""


class Rectangle:
    """
    The Rectangle Class:
    Has two internal properties, and two methods to change them.
    Optional arguments specify the width and height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """define object width and height"""

        if not isinstance(width, int) or not isinstance(height, int):
            wrong = 'width' if not isinstance(width, int) else 'height'
            raise TypeError(wrong + ' must be an integer')
        if width < 0 or height < 0:
            wrong = 'height' if height < 0 else 'width'
            raise ValueError(wrong + ' must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get access to private instance width
        return width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Raise Typeerror if width is not integer
        valueerror if width is less than 0"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get access to private instance height
        return height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Raise Typeerror if width is not integer
        valueerror if width is less than 0"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
