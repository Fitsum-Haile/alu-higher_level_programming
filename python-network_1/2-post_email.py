#!/usr/bin/python3

"""
Sends a POST request to a specified URL with email data.

This module takes two command-line arguments:
1. URL of the target endpoint.
2. Email address to be sent in the POST request.

The module constructs a POST request with the
provided email data, sends it to the specified URL,
and prints the response body to the console.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    dta = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(url, dta)
    with urllib.request.urlopen(req) as ans:
        print(ans.read().decode("utf-8"))
