#!/usr/bin/python3
""" A class  developed """


class BaseGeometry:
    """BaseGeometry class for geometric calculations."""

    def integer_validator(self, name, value):
        """
        Validate if the value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.
        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string describing the rectangle.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Square class that inherits from Rectangle."""
    def __init__(self, size):
        """
        Initialize the Square with size.
        Args:
        size (int): The size of the rectangle.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.
        """
        sq = self._Rectangle__width
        return ("[Square] {}/{}".format(sq, sq))
