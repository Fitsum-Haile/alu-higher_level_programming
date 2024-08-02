#!/usr/bin/python3
"""
Fetches and displays the status of https://alu-intranet.hbtn.io/status.

The script uses the urllib package to fetch the URL and prints the
response details including the type of content, the content itself,
and the UTF-8 decoded content.
"""

import urllib.request

def main():
    """
    Fetches data from the specified URL and prints the response details.

    The function uses the urllib.request.urlopen method to get the
    response from the URL, reads the content, and prints:
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
    main()
