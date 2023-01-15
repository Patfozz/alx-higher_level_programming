#!/usr/bin/python3
'''
Defines the class Square
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle

    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes the Square object

        Args:
            size (int): size of the square
            x (int): position on the x axis
            y (int): position on the y axis
            id (int): the id of the object
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns a string representation of a Square object

        '''
        return ('[Square] ({:d}) {:d}/{:d} - {:d}'.
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        '''Returns the size of the Square object

        Return:
            returns the size
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''Sets the size of the Square object

        Args:
            value (int): the new size value
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Updates the Square instance

        Args:
            list of new values to update Square values
        '''
        if args:
            keys = ['id', 'size', 'x', 'y']
            for key, value in zip(keys, args):
                setattr(self, key, value)
            return
        else:
            for key, value in kwargs.items():
                if key in kwargs.keys():
                    setattr(self, key, value)

    def to_dictionary(self):
        '''Returns a dictionary representation of a Square

        Return:
            returns the dictionary representation
        '''
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
