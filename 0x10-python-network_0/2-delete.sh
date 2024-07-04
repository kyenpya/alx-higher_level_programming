#!/bin/bash
# Sends a DELETE request to the URL as the first argument then displays the body of the respons
curl -s -X DELETE "${1}"
