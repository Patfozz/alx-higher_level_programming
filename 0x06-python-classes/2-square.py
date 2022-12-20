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
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
