#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(k, val)) for k, val in sorted(a_dictionary.items())]
