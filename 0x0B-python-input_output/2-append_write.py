#!/usr/bin/python3
""" A module hat appends """


def append_write(filename="", text=""):
    """
    Appends a string
    returns the text length
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return (len(text))
