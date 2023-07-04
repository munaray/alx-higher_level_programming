#!/usr/bin/python3
"""A function that adds two integers."""


def add_integer(a, b=98):
    """a and be must be integer otherwise raise TypeError
    If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
