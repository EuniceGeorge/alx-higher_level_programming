#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.
"""


class Square:
    """
    a class that perform square.

    Attributes:
        size(int): The number to passed.
        """
    def __init__(self, size):

        """
        initialization of square number
        Args:
        size(int): the number
        """
        self.__size = size
