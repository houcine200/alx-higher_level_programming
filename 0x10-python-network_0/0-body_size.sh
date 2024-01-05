#!/bin/bash

# Fetches the "Content-Length" from the HEAD response of 0.0.0.0:5000
curl -sI 0.0.0.0:5000 | grep Content-Length | cut -d ' ' -f2
