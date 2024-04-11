#!/usr/bin/python3
"""
The Rectangle Module:
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    """
    The Rectangle Class:
    Has two internal properties, and two methods to change them.
    Optional arguments specify the width and height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        takes in private instances width and height
        """
        if not isinstance(width, int) or not isinstance(height, int):
            wrong = 'width' if not isinstance(width, int) else 'height'
            raise TypeError(wrong + ' must be an integer')
        if height < 0 or width < 0:
            wrong = 'width' if width < 0 else 'height'
            raise ValueError(wrong + ' must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        string = ''
        if self.__height > 0 or self.__width > 0:
            for _ in range(self.__height):
                for _ in range(self.__width):
                    string += str(self.print_symbol)
                string += '\n'
            return (string[: -1])
        else:
            return ("")

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__height, self.__width))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
