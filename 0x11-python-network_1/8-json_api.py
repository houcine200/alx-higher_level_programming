#!/usr/bin/python3
from sys import argv
import requests

if __name__ == '__main__':
    if len(argv) < 2:
        av1 = ""
    else:
        av1 = argv[1]
    
    data = {'q': av1}
    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_data = r.json()
        if not json_data:
            print('No result')
        else:
            print(f"[<{json_data['id']}>] <{json_data['name']}>")
    except ValueError:
        print("Not a valid JSON")
