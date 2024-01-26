#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument in the body,
# and displays the body of the response.

# Check if URL and filename arguments are provided.
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Read the content of the file.
content=$(cat "$2")

# Send POST request to URL with file content in the body, and display body of response.
curl -s -X POST -d "$content" -H "Content-Type: application/json" "$1"
