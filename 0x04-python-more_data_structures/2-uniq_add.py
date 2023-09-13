#!/usr/bin/python3
def uniq_add(my_list=[]):

    my_set = set(my_list)
    Sum = 0

    for n in my_set:
        Sum += n
    return Sum
