#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """Class that defines a square.

    Attributes:
         size (str): Size of the Square
     """
    def __init__(self, size=0):
        """Initializer function for a Square.

        Args:
            size (int): Size of the Square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the Square.

        Returns:
            The area of the Square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Gets private __size attribute.

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a new value for __size attribute.

        Args:
        value (int): The value of the new size.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
