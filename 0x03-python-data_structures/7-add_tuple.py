#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a = [0, 0]
    if len(tuple_b) == 0:
        b = [0, 0]
    if len(tuple_a) == 1:
        a = list(tuple_a)
        a.append(0)
    if len(tuple_b) == 1:
        b = list(tuple_b)
        b.append(0)
    if len(tuple_a) > 1:
        a = list(tuple_a)
    if len(tuple_b) > 1:
        b = list(tuple_b)

    result = [a[0] + b[0], a[1] + b[1]]
    return tuple(result)
