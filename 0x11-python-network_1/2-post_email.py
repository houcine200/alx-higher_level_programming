#!/usr/bin/python3
'''Sends a POST request to a specified URL with an email parameter,
 and displays the decoded content of the response'''

from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    url = argv[1]
    params = {'email': argv[2]}
    querystring = parse.urlencode(params)
    data = querystring.encode('utf-8')

    with request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
    print(content)
