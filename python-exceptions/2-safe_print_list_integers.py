#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print("")  # Newline after printing integers
    except IndexError:
        import traceback
        traceback.print_exc(limit=0, file=sys.stdout)
        raise IndexError("list index out of range")
    return count
