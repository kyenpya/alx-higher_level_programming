#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_element = []

    for num in my_list:
        if num == search:
            num = replace
            new_element.append(num)
        else:
            new_element.append(num)

    return new_element
