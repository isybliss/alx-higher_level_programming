#!/usr/bin/python3
import hidden_4

def discov():
    import sys
    name = dir(hidden_4)
    for n in name:
        if n[:2] != '__':
            print(n)

if __name__ == "__main__":
    discov()
