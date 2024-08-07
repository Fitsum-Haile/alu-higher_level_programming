#!/usr/bin/python3
"""Lists the 10 most recent commits for a given repository and owner."""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit", {}).get("author", {}).get("name")))
    except IndexError:
        pass
