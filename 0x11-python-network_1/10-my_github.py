#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    response = requests.get('https://api.github.com/user', auth=(yoniem, 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))
    
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)
