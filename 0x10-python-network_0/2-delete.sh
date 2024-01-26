#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument using curl,
# and displays the body of the response.

# Check if URL argument is provided.
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request to URL and display body of response
curl -s -X DELETE "$1"
