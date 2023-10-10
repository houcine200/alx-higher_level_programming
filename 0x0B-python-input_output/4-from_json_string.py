#!/usr/bin/python3
""" return an object (Python data structure) represented by a JSON string """


import json
"""return a JSON string to a PYTHON data"""
def from_json_string(my_str):
    return json.loads(my_str)