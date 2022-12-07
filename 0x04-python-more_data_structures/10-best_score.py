#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest = max(my_dict.values())
    for key, value in my_dict.items():
        if value is biggest:
            return key
