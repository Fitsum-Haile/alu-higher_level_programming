#!/usr/bin/python3
"""Fetches url"""
import requests


if __name__ == "__main__":
    req = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format((req.text)))
