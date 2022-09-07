#!/usr/bin/python3
for x in range(9):
    for y in range(x, 10):
        if x != 9:
            print('{}{}'.format(x, y), end=", ")
        else:
            print('{}{}'.format(x, y))

