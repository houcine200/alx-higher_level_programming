#!/usr/bin/python3
'''Sends a GET request to url using the 'requests' library,
prints details about the HTTP response, including type and content.'''
import requests

html = requests.get('https://alx-intranet.hbtn.io/status')

print("Body response:")
print(f"\t- type: {type(html.text)}")
print(f"\t- content: {html.text}")
