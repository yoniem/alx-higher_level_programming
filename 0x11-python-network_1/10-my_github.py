#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(yoniem, 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
))

    if response.status_code == 200:
        user_info = response.json()
        print("Your GitHub user ID is:", user_info['yoniem'])
    else:
        print("Failed to fetch user ID. Status code:", response.status_code)
