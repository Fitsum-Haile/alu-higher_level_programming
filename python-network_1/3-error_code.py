#!/usr/bin/python3

"""
Fetches and displays the content of a URL provided as a command-line argument

This script takes a single URL as input from the command line.
It then attempts to access the URL
using the `urllib.request` module.
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as ans:
            print(ans.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
