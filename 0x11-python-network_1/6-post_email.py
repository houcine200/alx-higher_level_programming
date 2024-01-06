#!/usr/bin/python3
''' Sends a POST request to  URL with provided email as a parameter,
 retrieves the content of the HTTP response, and prints it.'''
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    r = requests.post(url, data)
    print(r.text)
