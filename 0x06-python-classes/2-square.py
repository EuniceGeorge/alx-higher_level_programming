#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module carries out the operation'square' for each input.
"""


class Square:
    """
    a class that perform square.

    Attributes:
        size(int): The number to passed.
        """
    def __init__(self, size=0):
        """
         initialization of square number
         Args:
             size(int):The size of the square's side

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
