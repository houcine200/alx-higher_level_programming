#!/bin/bash
# send a POST request with form data including email and subject to specified URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
