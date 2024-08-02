#!/usr/bin/python3
"""
Module to fetch and display the status of a given URL.

This module uses urllib to fetch the content from https://alu-intranet.hbtn.io/status
and prints the content type, the raw content, and the UTF-8 decoded content.
"""

import urllib.request

def fetch_status():
    """
    Fetches and displays the status of the URL.

    Uses urllib.request to get the response from the URL, then reads and
    prints:
    - The type of the response body.
    - The raw content of the response.
    - The UTF-8 decoded content of the response.
    """
    url = 'https://alu-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
