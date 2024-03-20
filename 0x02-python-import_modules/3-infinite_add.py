#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    for ag in argv[1:]:
        result += int(ag)
    print('{:d}'.format(result))
