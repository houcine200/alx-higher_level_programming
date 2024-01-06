#!/usr/bin/python3
'''Fetches and prints details about the content from url
 including type, raw bytes, and UTF-8 decoded content.'''
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

print("Body response:")
print(f"\t- type: {type(html)}")
print(f"\t- content: {html}")
print(f"\t- utf8 content: {html.decode('utf-8')}")
