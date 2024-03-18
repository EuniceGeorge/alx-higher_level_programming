#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 0:
        return (1)
    elif b == 1:
        return (a)
    elif b < 0:
        a = 1 / a
        b = -b
    while b > 0:
        if b % 2 == 1:
            result *= a
            a *= a
            b //= 2
    return (result)
