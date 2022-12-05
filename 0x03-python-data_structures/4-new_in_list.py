#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Make copy of a list, reolace element t a certain index in copy
        while leaving original unmodified.
    """
    new_list = my_list[:]

    if idx < o or idx > (len(my_list) - 1)):
        return (my_list[:])

    new_list[idk] = element
    return (new_list)
