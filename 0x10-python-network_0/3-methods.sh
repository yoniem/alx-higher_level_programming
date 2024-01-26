#!/bin/bash
# This script takes a URL as input and displays all HTTP methods accepted by the server

# Check if URL argument is provided..
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send an OPTIONS request to the URL and display allowed HTTP methods
curl -s -X OPTIONS -i "$1" | awk '/Allow:/ {print substr($0, index($0,$2))}'
