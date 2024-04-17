#!/usr/bin/python3
""" A module that writes a string to a text file """



def write_file(filename="", text=""):
    """
    open a file
    write a content to a file
    """

    with open("filename", "w") as f:
        content = f.write(text)
        return content
