#!/bin/bash
# Sends a request to the URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep -i "Allow:"
