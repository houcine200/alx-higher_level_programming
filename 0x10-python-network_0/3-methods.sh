#!/bin/bash
# Use curl to fetch the HTTP headers, extract the 'Allow' header, and display its values
curl -sI "$1" | grep Allow | cut -d ' ' -f2,3,4
