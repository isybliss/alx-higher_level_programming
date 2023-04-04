#!/usr/bin/python3
"""
script that takes in a url, send request to the url and displays body
of the response. if http status code is >= 400, print Error code:
followed by HTTP status code. use sys and urllib package and with statement
"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    f = requests.get(url)
    status = f.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(f.text)
