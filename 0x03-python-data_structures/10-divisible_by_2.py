#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    answer = []
    for element in my_list:
        if element % 2 == 0:
            answer.append(True)
        else:
            answer.append(False)
    return answer
