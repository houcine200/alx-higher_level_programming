#!/bin/bash
# Use curl to send a POST request with form data including email and subject to the specified URL
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"