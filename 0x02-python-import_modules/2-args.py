#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    val = ""
    argc = len(argv) - 1
    if argc > 1:
        delim = "s:"
    elif argc == 0:
        delim = "s."
    else:
        delim = ":"
    for i, ag in enumerate(argv[1:]):
        val += '{:d}: {}\n'.format(i+1, ag)
    print('{:d} argument{}\n{}'.format(argc, delim, val), end="")
