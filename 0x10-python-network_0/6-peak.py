#!/usr/bin/python3
""" module doc """


def find_peak(list_of_integers):
    """ Finds a peak in an unsorted array """

    if not list_of_integers:
        return None

    first = 0
    second = len(list_of_integers) - 1

    while first < second:
        mid = (first + second) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            second = mid
        else:
            first = mid + 1

    return list_of_integers[first]
