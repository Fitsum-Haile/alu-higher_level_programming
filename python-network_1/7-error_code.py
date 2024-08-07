#!/usr/bin/python3
"""Sends a request to a URL and displays the response body or error code."""

import sys
import requests


def fetch_url(url):
    """
    Sends a GET request to the given URL and handles the response.
    Args:
    url (str): The URL to send the request to.
    Prints:
    - The body of the response if the status code is less than 400.
    - 'Error code: [status code]' if the status code is 400 or greater.
    """
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    # Extract URL from command-line arguments
    url = sys.argv[1]
    # Fetch URL and display response or error code
    fetch_url(url)
