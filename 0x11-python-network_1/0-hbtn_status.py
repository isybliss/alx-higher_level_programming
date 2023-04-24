#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
using urllib package
with statement must be used
"""


if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('http://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as f:
        status = f.read()
        print("Body response:")
        print("\t- type: {}".format(type(status)))
        print("\t- content: {}".format(status))
        print("\t- utf8 content: {}".format(status.decode('utf-8')))
