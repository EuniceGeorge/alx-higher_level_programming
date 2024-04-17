#!/usr/bin/python3
"""
A function that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """ a function to convert to json"""
    import json

    json_string = json.dumps(my_obj)
    return json_string
