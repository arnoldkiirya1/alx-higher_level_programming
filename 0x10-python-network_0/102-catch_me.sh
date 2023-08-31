#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me using curl,
# and displays the body of the response.

# Send a request to the specified URL and display the body of the response
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"
