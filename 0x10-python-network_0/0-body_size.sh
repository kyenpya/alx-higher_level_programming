#!/bin/bash

# Script takes a URL, sends a request and displays the size of the body of the response

curl -s "${1}" | wc -c
