#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index in row:
            if index != row[-1]:
                print("{:d}".format(index), end=" ")
            else:
                print("{:d}".format(index), end="")
        print()
