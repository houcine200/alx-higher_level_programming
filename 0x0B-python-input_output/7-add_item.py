#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    j_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    j_list = []

for i in argv[1:len(argv)]:
    j_list.append(i)

save_to_json_file(j_list, 'add_item.json')
