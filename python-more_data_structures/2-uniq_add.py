#!/usr/bin/python3


def uniq_add(my_list=[]):
    # Use a set to store unique elements and sum them up
    unique_elements = set(my_list)
    result = sum(unique_elements)
    return result
