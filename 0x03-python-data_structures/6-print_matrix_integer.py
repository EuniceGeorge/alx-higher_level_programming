#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            i = 0
            if i == len(row):
                print('{:d}'.format(element), end="")
            print('{:d}'.format(element), end=" ")
            i += 1
        print()    
