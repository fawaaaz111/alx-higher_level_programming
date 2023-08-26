#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):

    for row in matrix:
        for item in row:
            print(str.format("{:d} ", item), end=' ')
        print()

