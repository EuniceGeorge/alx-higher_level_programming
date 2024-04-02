#!/usr/bin/python3
def raise_exception():
    try:
        result = 1 + 'a'
    except TypeError as te:
        raise te

