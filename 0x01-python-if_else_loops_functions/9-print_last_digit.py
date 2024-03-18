#!/usr/bin/python3
def print_last_digit(number):
    r = number % 10
    r = r if r >= 0 else -r
    print('{:d}'.format(r), end='')
    return (r)
