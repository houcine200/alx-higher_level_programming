#!/bin/bash
# Sends a silent GET request to the specified URL and prints the HTTP status code.
curl -sw "%{http_code}" -o /dev/null "$1"
