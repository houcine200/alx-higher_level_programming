#!/bin/bash
# Sends a POST request with JSON data from the file 'my_json_0' to the specified URL.
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
