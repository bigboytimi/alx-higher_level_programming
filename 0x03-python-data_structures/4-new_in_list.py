#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    fresh_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return fresh_list
    else:
        fresh_list[idx] = element
        return fresh_list
