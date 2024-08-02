#!/bin/bash
# Sends a GET request to the URL and displays the body of a 200 status code response
curl -sL -w "%{http_code}" "$1" -o temp_body | { read code; [ "$code" -eq 200 ] && cat temp_body; rm -f temp_body; }
