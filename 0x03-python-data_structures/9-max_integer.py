#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        bigger_val = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > bigger_val:
                bigger_val = my_list[i]

        return bigger_val
