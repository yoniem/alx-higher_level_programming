#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': yonimphini@gmail.com}
    response = requests.post(url, data=data)

    print(response.text)
