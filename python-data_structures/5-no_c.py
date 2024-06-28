#!/usr/bin/python3


def no_c(my_string):
    str_list = list(my_string)
    for i in str_list:
        if i == 'c' or i == 'C':
            str_list[str_list.index(i)] = ''

    return ''.join(str_list)
