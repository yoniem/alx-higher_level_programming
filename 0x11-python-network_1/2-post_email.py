#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': yonimphini@gmail.com})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
