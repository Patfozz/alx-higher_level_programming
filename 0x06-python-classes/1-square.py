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
        self.__size = size
