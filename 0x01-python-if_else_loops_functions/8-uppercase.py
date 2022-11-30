#!/usr/bin/python3
def uppercase(str):
    for cha in str:
        if ord(cha) >= 97 and ord(cha) <= 122:
            char = chr(ord(cha) - 32)
            result = True
        else:
            result = False

        print("{:s}".format(char if result else cha), end="")
    print()
