#!/usr/bin/python3
'''Fetches the X-Request-Id variable from the header of
 the HTTP response for a given URL'''
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers["X-Request-Id"])
