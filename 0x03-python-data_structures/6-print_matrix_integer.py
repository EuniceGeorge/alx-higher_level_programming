#!/bin/usr/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for element in row:
            if i == len(row) -1:
                print('{:d}'.format(element), end="")
            print('{:d}'.format(element), end=" ")
            i += 1
        print()    
