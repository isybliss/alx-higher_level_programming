#!/usr/bin/python3

import sys


def main():
    argv = sys.argv
    arg_num = len(argv)
    i = 1
    res = 0

    while (i < arg_num):
        res += int(arg[i])
        i += 1

    print("{}".format(res))


    if __name__ == "__main__":
        main()
