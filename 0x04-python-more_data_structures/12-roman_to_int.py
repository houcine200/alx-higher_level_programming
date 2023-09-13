#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    rev = list(reversed(list(roman_string)))

    val = 0

    prev = 0

    for i in rev:
        curr = dic[i]

        if curr < prev:
            val = val - curr
        else:
            val = val + curr
        prev = curr
    return val
