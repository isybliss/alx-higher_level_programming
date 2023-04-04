#!/usr/bin/python3
"""
script that take in a url, sends a request to the url,displays the value
of the X-Request-Id variable found in the header of the response
use urllib and sys package and with statement
"""

import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as f:
        print(dict(f.headers).get("X-Request-Id"))
