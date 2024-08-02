#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter.

The script takes a URL and an email as command-line arguments,
sends a POST request with the email parameter, and displays
the response body decoded in UTF-8.
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Check that the script has been called with the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create the POST data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a request object
    request = urllib.request.Request(url, data=data, method='POST')

    # Send the request and display the response
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
