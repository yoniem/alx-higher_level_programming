#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl,
# and displays the size of the response body in bytes.

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to URL and display size of response body in bytes
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'
