#!/usr/bin/python3
"""
script that takes in a url and an email, sent a POST request to to the url
with email as parameter and displays the body of the response
use urllib and sys package. use with ststement
"""
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    """Data should be in bytes"""
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
