#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_num = len(argv)
    i = 1
    if arg_num == 0:
        print("{:d} arument.".format(arg_num))
        return
    else:
        if arg_num == 1:
            print("{:d} argument:".format(arg_num))
        else:
            print("{:d} arguments:".format(arg_num))

        while i < arg_number:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
