#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        reverse = my_list[-1:-(len(my_list) + 1):-1]
        for x in reverse:
            print("{:d}".format(x))
