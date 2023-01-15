#!/usr/bin/python3
'''
Defines the class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class that inherits from Base

    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes Rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): wasn't explained
            y (int): wasn't explained
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        '''Prints the rectangle

        '''
        return ('[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'
                .format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        '''Gets the width value

        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the width value

        Args:
            value (int): new value
        '''
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Gets the height value

        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the height value

        Args:
            value (int): new value
        '''
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''Gets the x value

        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets the x value
        Args:
            value (int): new value
        '''
        if isinstance(value, int) is False:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Gets the y value

        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''Sets the y value

        Args:
            value (int): new value
        '''
        if isinstance(value, int) is False:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Returns the area of the Rectangle

        Return:
            returns the area
        '''
        return self.width * self.height

    def display(self):
        '''Prints the rectangle to stdout

        '''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print('{:s}{:s}'.format(' ' * self.x, '#' * self.width))

    def update(self, *args, **kwargs):
        '''Updates the Rectangle instance

        Args:
            list of new values to update rectangle values
        '''
        if args:
            keys = ['id', 'width', 'height', 'x', 'y']
            for key, value in zip(keys, args):
                setattr(self, key, value)
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns a dictionary representation of a Rectangle

        Return:
            returns the dictionary representation
        '''
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
