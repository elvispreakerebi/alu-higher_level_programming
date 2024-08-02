#!/bin/bash
# Sends a GET request to the URL and displays the body of a 200 status code response
curl -s -o response_body.txt -w "%{http_code}" "$1" | grep -q 200 && cat response_body.txt
