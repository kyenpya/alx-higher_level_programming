#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dic = {}

    for key in a_dictionary:
        new_dic.update({key: a_dictionary.get(key) * 2})
    return new_dic
