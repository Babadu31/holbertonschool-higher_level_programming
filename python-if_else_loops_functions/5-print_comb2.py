#!/usr/bin/python3
for x in range(0, 99 + 1):
    print("{:0>2d}".format(x), end=", ")
    if x == 99:
        print(x)
