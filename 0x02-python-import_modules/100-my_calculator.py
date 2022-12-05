#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg_num = len(sys.argv) - 1
    if arg_num != 3:
        print("Usuage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op is '+':
        print("{} {} {} = {}".format(a, '+', b, add(a, b)))
    elif op is '-':
        print("{} {} {} = {}".format(a, '-', b, sub(a, b)))
    elif op is '*':
        print("{} {} {} = {}".format(a, '*', b, mul(a, b)))
    elif op is '/':
        print("{} {} {} = {}".format(a, '/', b, div(a, b)))
