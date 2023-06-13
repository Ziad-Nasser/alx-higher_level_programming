#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    max = my_list[0]
    for idx in my_list:
        if idx > max:
            max = idx
    return max
