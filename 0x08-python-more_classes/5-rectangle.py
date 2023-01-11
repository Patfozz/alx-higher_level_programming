#!/usr/bin/python3
""" initializing the call"""


class Rectangle:
    """ Defining Rectangle"""

    def __init__(self, width=0, height=0):

        """ defining a new rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):

        """ defineing width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getting and setting hieght"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """defing area """

        return(self.__height * self.__width)

    def perimeter(self):
        """getting perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """returns printable

        characters for the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):

        """returns string representation of the rectangle"""

        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print massage when ever a rectangle is deleted"""

        print("Bye rectangle...")
