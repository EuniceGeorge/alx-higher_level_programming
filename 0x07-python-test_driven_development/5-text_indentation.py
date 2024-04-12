#!/usr/bin/python3
"""
A module that prints text"""


def text_indentation(text):
    """
    text_indentation function:
    checks to see if input is valid
    adds two new lines after any instances of `?` or `.` or `:`
    then prints the result without any new lines at the beginning
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for words in text:
        result += words
        if words in (".", "?", ":"):
            result += "\n\n"
    print(result)
