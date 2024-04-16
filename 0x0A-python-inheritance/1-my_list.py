#!/usr/bin/python3
""" A function"""


class MyList(list):
    """ A class that inherits from List"""
    def print_sorted(self):
        print(sorted(self))
