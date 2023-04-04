#!/usr/bin/python3
"""
script that take in a url, sends a request to the url,displays the value
of the X-Request-Id variable found in the header of the response
use requests and sys package
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    f = requests.get(url)
    print(f.headers.get("X-Request-Id"))
