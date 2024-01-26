#!/bin/bash
# This script takes a URL as input, sends a GET request to that URL using curl,
# with the header X-School-User-Id set to 98, and displays the body of the response

# Check if URL argument is provided.
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request to URL with header X-School-User-Id set to 98, and display body of response.
curl -s -H "X-School-User-Id: 98" "$1"
