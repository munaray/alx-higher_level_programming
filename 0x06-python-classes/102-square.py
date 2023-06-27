#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """This represent a square."""

    def __init__(self, size=0):
        """Initialize a new square with size arg"""
        self.size = size

    @property
    def size(self):
        """This get/set the current square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """== comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """!= comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """< comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """<= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """> comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """>= compmarison to a Square."""
        return self.area() >= other.area()
