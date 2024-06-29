#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least two elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Create the result tuple by adding corresponding elements
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
