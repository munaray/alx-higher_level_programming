#!/usr/bin/python3
"""A function that prints My name is <firstname> <lastname>"""


def say_my_name(first_name, last_name=""):
    """Passing first and last name as arg, raise TypeError
    if either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
