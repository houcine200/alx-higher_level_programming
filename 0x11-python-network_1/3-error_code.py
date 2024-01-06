#!/usr/bin/python3
'''Fetches the content from a specified URL, prints it if successful,
 or prints the HTTP status code if an error occurs'''
from sys import argv
from urllib import request

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')
        print(content)
    except Exception as err:
        print(f"Error code: {err.code}")
