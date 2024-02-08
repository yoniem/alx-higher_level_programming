#!/usr/bin/python3
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data.decode('utf-8'))
