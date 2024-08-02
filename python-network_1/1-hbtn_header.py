#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id variable from the header of the response.

The script takes a URL as a command-line argument, sends a request to the URL,
and prints the value of the X-Request-Id header found in the response.
"""

import sys
import urllib.request

def fetch_request_id(url):
    """
    Sends a request to the specified URL and prints the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    with urllib.request.urlopen(url) as response:
        # Get the value of the X-Request-Id header
        request_id = response.getheader('X-Request-Id')
        print(request_id)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        fetch_request_id(url)
