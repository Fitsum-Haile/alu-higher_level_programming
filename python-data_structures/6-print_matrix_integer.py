#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            for i in range(len(row)):
                if i == len(row) - 1:
                    print("{:d}".format(row[i]), end="")
                else:
                    print("{:d} ".format(row[i]), end="")
            print()
        else:
            print()
