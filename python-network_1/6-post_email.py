#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response."""

import sys
import requests


def post_email(url, email):
    """
    Sends a POST request with the email as a parameter.
    
    Args:
    url (str): The URL to which the POST request is sent.
    email (str): The email address to send in the POST request.
    Returns:
    str: The body of the response from the POST request.
    """
    response = requests.post(url, data={'email': email})
    return response.text

if __name__ == "__main__":
    # Extract URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Send POST request and print the response body
    print(post_email(url, email))
