#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None

    maxi = my_list[0]
    for element in my_list:
        if element > maxi:
            maxi = element
    return maxi
