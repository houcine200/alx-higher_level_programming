#!/usr/bin/python3

for alpha in range(97, 123):
    if (alpha != ord('e') and alpha != ord('q')):
        print("{}".format(chr(alpha)), end="")
