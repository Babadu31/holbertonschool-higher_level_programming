#!/usr/bin/python3
"""
Add Integer or Float
"""


def add_integer(a, b=98):
    """
    ADD Two integer a and b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if (a + b) == float('inf') or (a + b) == -float('inf'):
        return b
    return int(a) + int(b)
