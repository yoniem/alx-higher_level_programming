#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response

# Check if URL argument is provided.
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to URL and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
