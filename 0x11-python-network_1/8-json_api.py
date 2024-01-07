#!/usr/bin/python3
'''
Sends a POST request to URL with a search letter as a parameter.
If the response contains valid JSON, displays the id and name,
otherwise handles errors.
'''
from sys import argv
import requests

if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    data = {'q': av1}
    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_data = r.json()
        if 'id' not in json_data or 'name' not in json_data:
            print('No result')
        else:
            id = json_data.get('id')
            name = json_data.get('name')
            print(f"[<{id}>] <{name}>")
    except ValueError:
        print("Not a valid JSON")
