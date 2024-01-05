#!/bin/bash

# This script sends a HEAD request to 0.0.0.0:5000 using curl,
# retrieves the "Content-Length" header using grep and cut,
# and prints the extracted content length to the console.
curl -sI 0.0.0.0:5000 | grep Content-Length | cut -d ' ' -f2
