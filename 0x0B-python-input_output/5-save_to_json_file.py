#!/usr/bin/python3
""" A module to write to a json file """


def save_to_json_file(my_obj, filename):
    """ A function
    write to a text file
    """

    import json

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
