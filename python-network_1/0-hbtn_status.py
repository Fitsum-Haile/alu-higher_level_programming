#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status and prints the response details."""

import urllib.request

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # Adjusted URL for local testing
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except Exception as e:
        print(f"An error occurred: {e}")
