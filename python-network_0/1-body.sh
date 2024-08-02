#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" -o /tmp/response_body | grep -q "200$" && cat /tmp/response_body
