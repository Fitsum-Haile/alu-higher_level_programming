#!/usr/bin/python3
"""Sends a POST request with a letter and processes the JSON response."""

import sys
import requests


if __name__ == "__main__":
    # Get the letter from command-line arguments or default to an empty string
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    # Send the POST request
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        # Try to parse the JSON response
        result = response.json()
        if not result:
            print("No result")
        else:
            user_id = result.get("id")
            name = result.get("name")
            if user_id is None or name is None:
                print("No result")
            else:
                print("[{}] {}".format(user_id, name))
    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")
