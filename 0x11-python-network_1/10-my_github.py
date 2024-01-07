#!/usr/bin/python3
'''
Uses Basic Authentication with GitHub API to display the user's id.
Takes GitHub credentials (username and personal access token) as arguments.
'''
import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(username, password))
    print(r.json().get('id'))
