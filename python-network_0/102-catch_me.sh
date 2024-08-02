#!/bin/bash
# Makes a request to the specified URL and causes the server to respond with "You got me!"
curl -s -X PUT -H "Origin: School" http://0.0.0.0:5000/catch_me
