#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index in row:
            if index != row[-1]:
                print("{}".format(index), end=" ")
            else:
                print("{}".format(index), end="")
        print()
