#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """This represent a square."""

    def __init__(self, size=0):
        """Initialize a new square with size args"""
        self.size = size

    @property
    def size(self):
        """To get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)
