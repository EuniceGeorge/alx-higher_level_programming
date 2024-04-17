#!/usr/bin/python3
"""
A module that writes a string to a text file
return number of xter written
"""


def write_file(filename="", text=""):
    """
    write text to file
    return number of character
    """
    with open(filename, 'w', encoding='utf-8') as f:
        content = f.write(text)
        return content
