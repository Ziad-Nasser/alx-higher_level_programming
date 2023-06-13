#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for column in matrix:
            print("{:d}".format(column), end=" " if column != rows[-1] else "")
        print()
