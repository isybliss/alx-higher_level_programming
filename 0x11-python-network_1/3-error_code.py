#!/usr/bin/python3
"""
script that takes in a url, send request to the url and displays body
of the response. manage urllib.error.HTTPError exception, print Error code:
followed by HTTP status code. use sys and urllib package and with statement
"""

import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
