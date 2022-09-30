#!/usr/bin/python3
"""
writes a string to a text file (UTF8)
and returns the number of characters
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
