#!/usr/bin/python3
""" a module that creates an object file """


def load_from_json_file(filename):
    """
    A function that creates an object file"""

    import json

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
