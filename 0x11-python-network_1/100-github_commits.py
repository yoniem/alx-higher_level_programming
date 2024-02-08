#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{yoniem}/{alx-higher_level_programming}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]  # Limit to the most recent 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['yoniem']
            print(f"{sha}: {yoniem}")
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")

