#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            index += 1
        except IndexError:
            print()
            return index
    print()
    return index

"""
    try:
        index = 0
        for i in range(x):
            print(my_list[i], end="")
            index += 1
     except IndexError:
        pass
     finally:
        print()
        return index
"""
