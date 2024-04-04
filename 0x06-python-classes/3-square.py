#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module create a class Square gets the square of an input
"""


class Square:
    """
    A class that represents a square and calculates its area.

    Attributes:
    - size (int): The size of the square's side.

    Methods:
    - __init__(size=0): Initializes the Square instance with a specified size.
    - area(): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a specified size.

        Parametrs:
        - size (int): The size of the square's side. Default is 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square (size squared).
        """
        return self.__size ** 2
