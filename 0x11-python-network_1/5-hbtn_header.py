#!/usr/bin/python3
'''Sends a GET request to the specified URL using the 'requests' library,
retrieve and print value of'X-Request-Id' header from the HTTP response'''

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
