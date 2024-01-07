#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of a repository on GitHub.
Usage: ./10-commits.py <repository> <owner>
"""
import requests
from sys import argv

if __name__ == "__main__":
    repository = argv[1]
    owner = argv [2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    
    r = requests.get(url)
    commits = r.json()[:10]
    
    for commit in commits:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print(f"{sha}: {name}")
