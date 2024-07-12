#!/usr/bin/python3

class LockedClass:
    __slots__ = ['first_name']

# Example Usage (101-main.py)
if __name__ == "__main__":
    LockedClass = __import__('101-locked_class').LockedClass

    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
