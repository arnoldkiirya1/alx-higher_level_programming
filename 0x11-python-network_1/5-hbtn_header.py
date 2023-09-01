#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    # Check if the 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
