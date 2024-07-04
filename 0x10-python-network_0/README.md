# 0x10. Python - Network #0

## Description

This project involves understanding and working with HTTP (HyperText Transfer Protocol) using Bash and Python. The tasks include making HTTP requests, handling HTTP responses, and implementing HTTP methods using cURL.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All scripts will be tested on Ubuntu 20.04 LTS
- Bash scripts should be exactly 3 lines long
- All files should end with a new line
- All files must be executable
- The first line of all Bash scripts should be exactly `#!/bin/bash`
- The second line of all Bash scripts should be a comment explaining what the script does
- All curl commands must use the `-s` option (silent mode)
- Python files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all Python files should be exactly `#!/usr/bin/python3`
- Code should follow the pycodestyle (version 2.8.*)
- All modules should be documented
- All classes should be documented
- All functions (inside and outside a class) should be documented

## Project Tasks

### Task 0: cURL body size

- **File:** `0-body_size.sh`
- **Description:** Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

### Task 1: cURL to the end

- **File:** `1-body.sh`
- **Description:** Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response for a 200 status code response.

### Task 2: cURL Method

- **File:** `2-delete.sh`
- **Description:** Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

### Task 3: cURL only methods

- **File:** `3-methods.sh`
- **Description:** Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

### Task 4: cURL headers

- **File:** `4-header.sh`
- **Description:** Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable `X-School-User-Id` must be sent with the value `98`.

### Task 5: cURL POST parameters

- **File:** `5-post_params.sh`
- **Description:** Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. Variables `email` and `subject` must be sent with specified values.

### Task 6: Find a peak

- **File:** `6-peak.py`, `6-peak.txt`
- **Description:** Write a function that finds a peak in a list of unsorted integers. The algorithm must have the lowest complexity possible.
