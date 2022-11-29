#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result = result + chr(ord(char) - 32)
        else:
            result = result + char
        print("{:s}".format(result))
