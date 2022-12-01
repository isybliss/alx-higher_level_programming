#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    arg_num = len(argv) - 1
    i = 1
    result = 0
    if arg_mun == 0:
        print("{:d}".format(arg_num))
        return
    else:
        while i <= arg_num:
            result += int(argv[i])
            i += 1
        print("{:d}".format(add))
