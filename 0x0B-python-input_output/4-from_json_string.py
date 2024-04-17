#!/usr/bin/python3
""" A module that returns an object """


def from_json_string(my_str):
    """
    a function that returns aan object
    """
    import json

    j_str = json.loads(my_str)
    return j_str
