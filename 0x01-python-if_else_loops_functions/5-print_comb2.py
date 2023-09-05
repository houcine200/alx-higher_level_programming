#!/usr/bin/python3

for n in range(0, 100):
    print("{}{}".format(int(n / 10), int(n % 10)), end="")
    print(end=", " if n != 99 else "\n")
