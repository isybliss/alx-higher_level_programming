#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    while True:
        try:
            if index < x:
                print(my_list[index], end='')
                index += 1
            print()
        except IndexError:
            print()
        finally:
            return index
"""
            else:
                print()
                return index
        except IndexError:
            print()
            return index
"""
