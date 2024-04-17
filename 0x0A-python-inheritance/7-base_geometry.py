#!/usr/bin/python3
""" A function based on previous """


class BaseGeometry:
    """ A class with two instances, area and integer_validation"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A method for validation """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
