#!/bin/bash
# Sends GET request to URL with custom header "X-School-User-Id: 98" using curl.
curl -sH "X-School-User-Id: 98" "$1"
