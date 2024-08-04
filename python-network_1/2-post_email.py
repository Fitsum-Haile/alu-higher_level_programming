#!/usr/bin/python3

"""SENDS A POST REQUEST"""

import requests  # Replace urllib with requests

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}  # Use data instead of val for clarity

    # Use requests.post for simpler POST request
    response = requests.post(url, data=data)

    # Print the response content
    print(response.text)
