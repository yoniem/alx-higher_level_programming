#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_value = response.headers.get('X-Request-Id')
        print(header_value)
