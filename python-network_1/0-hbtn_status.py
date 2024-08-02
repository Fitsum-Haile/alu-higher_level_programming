#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and prints the response details."""

import urllib.request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"  # Ensure this URL is correct
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URLError: {e.reason}")
