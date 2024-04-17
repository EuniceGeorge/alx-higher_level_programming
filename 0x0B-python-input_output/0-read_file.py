#!/usr/bin/python3
""" A function that reads text file """


def read_file(filename=""):
    """
    reads a file
    prints it to stdout
    """

    with open(filename, 'r', encoding="utf-8") as file_n:
        content = file_n.read()
        print(content, end="")
