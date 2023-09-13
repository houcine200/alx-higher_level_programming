#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    tot, Sum = 0, 0
    for tupl in my_list:
        Sum += (tupl[0] * tupl[1])
        tot += tupl[1]
    av = Sum / tot
    return av
