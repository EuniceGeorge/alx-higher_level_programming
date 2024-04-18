#!/usr/bin/python3
""" A function that adds all arguments """


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
Retrieve arguments and convert to list
load existing list from file
"""

argument = sys.argv.pop(0)

try:
    existing = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing = []

combined = existing + argument

save_to_json_file(combined, "add_item.json")
