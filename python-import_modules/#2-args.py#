#!/usr/bin/python3
import sys


def main(*argv):
    x = 0
    y = len(sys.argv) - 1
    if y == 1:
        print("{:d} argument:".format(y))
    elif y == 0:
        print("{:d} arguments.".format(y))
    else:
        print("{:d} arguments:".format(y))
    for args in sys.argv:
        if (x != 0):
            print("{}: {}".format(x, args))
        x += 1


if __name__ == "__main__":
    main()
