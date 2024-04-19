#!/usr/bin/python3
""" A function"""


class MyList(list):
    """
    A class that inherits from List
    prints the sorted list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
