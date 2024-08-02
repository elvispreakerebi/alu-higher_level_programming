#!/bin/bash
# Check if URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send a request to the URL and display the size of the body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$URL"

