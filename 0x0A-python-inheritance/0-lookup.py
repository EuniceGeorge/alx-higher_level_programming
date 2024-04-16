#!/usr/bin/python3
""" A function to get the list of an object"""


def lookup(obj):
    """ A function 'lookup' with argument 'obj'
    Get the list of attributes and methods of the object"""
    attributes_methods = dir(obj)
    return attributes_methods
