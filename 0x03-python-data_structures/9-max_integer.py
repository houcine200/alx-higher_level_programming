#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxi = my_list[0]
    for n in my_list:
        if n > maxi:
            maxi = n
    return maxi
