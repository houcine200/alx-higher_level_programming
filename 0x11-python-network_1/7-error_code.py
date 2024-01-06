#!/usr/bin/python3
'''Sends a GET request to URL using 'requests' library, print content of
HTTP response or the error code if the status code is 4xx or higher.'''

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if (r.status_code >= 400):
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
