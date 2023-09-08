#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for ch in my_string:
        if ch not in my_string:
            s += ch
    return s
