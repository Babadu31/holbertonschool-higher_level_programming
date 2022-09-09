#!/usr/bin/python3
import sys


def main(*argv):
    x = 0
    l = len(sys.argv) - 1
    if l == 1:
        print("{:d} argument:".format(l))
    elif l == 0:
        print("{:d} arguments.".format(l))
    else:
        print("{:d} arguments:".format(l))
    for args in sys.argv:
        if (x != 0):
            print("{}: {}".format(x, args))
        x += 1

if __name__ == "__main__":
    main()
