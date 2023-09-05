#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != 8:
            print("{}{}".format(int(i), int(j)), end=", ")
        else:
            print("{}".format(89), end="\n")
