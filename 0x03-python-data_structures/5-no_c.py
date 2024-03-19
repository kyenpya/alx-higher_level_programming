#!/usr/bin/python3


def no_c(my_string):
    copy = ""
    for ch in my_string:
        if ch != 'C' and ch != 'c':
            copy += ch
    return copy
