#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """Class that defines a square.

    Attributes:
         size (str): Size of the Square
     """
    def __init__(self, size=0, position=(0, 0)):
        """Initializer function for a Square.

        Args:
            size (int): Size of the Square.
            position (tuple): Position of the Square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of the Square.

        Returns:
            The area of the Square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #.
        """
        if self.size == 0:
            print()
        else:
            x, y = self.position
            for i in range(y):
                print()
            for i in range(self.size):
                print(' ' * x, end='')
                print('#' * self.size)

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

    @property
    def position(self):
        """Gets private __position attribute.

        Returns:
            The position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value for the __position attribute.

        Args:
            value (int): The value of the new position.
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if type(x) != int or type(y) != int or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
