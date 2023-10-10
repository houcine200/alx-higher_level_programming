#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    json_string = json.dumps(my_obj)
    
    with open(filename, "w") as file:
        file.write(json_string)
