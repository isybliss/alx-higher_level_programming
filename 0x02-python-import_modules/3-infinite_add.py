#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    arg_num = len(sys.argv) - 1
    result = 0
    for i in range(arg_num):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
