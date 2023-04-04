#!/usr/bin/python3
"""
script that fetches a url
"""


if __name__ == '__main__':
    import urllib.request

    request_url = 'http://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(request_url) as response:
        status = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(status)))
        print("\t- content: {}".format(status))
        print("\t- utf8 content: {}".format(status.decode('utf-8')))
