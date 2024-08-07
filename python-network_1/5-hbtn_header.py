#!/usr/bin/python3
"""Prints the 'X-Request-Id' header from a given URL."""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
