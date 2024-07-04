#!/usr/bin/python3


def raise_exception():
    raise TypeError

if __name__ == "__main__":
    raise_exception = __import__('5-raise_exception').raise_exception

    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
