#!/bin/bash
# Sends a GET request to the URL with a custom header and displays the body of the response
curl -s -v -H "X-HolbertonSchool-User-Id: 98" "$1" 2>&1 | grep -E '^< '
