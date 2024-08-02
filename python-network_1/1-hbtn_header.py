#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id variable from the header of the response.

The script takes a URL as a command-line argument, sends a request to the URL,
and prints the value of the X-Request-Id header found in the response.
"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
