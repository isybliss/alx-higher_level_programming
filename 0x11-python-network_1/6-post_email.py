#!/usr/bin/python3
"""
script that takes in a url and an email, sent a POST request to to the url
with email as parameter and displays the body of the response
use requests and sys package.
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    f = requests.post(url, data=values)
    print(f.text)
