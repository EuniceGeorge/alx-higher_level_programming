#!usr/bin/python3

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
             size(int): the number
             """

        if not isinstance(self, size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
