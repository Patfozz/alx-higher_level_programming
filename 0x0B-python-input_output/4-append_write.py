#!/usr/bin/python3
'''
Defines the append_write function
'''


def append_write(filename='', text=''):
    '''writes a string to the end of a text file

    Args:
        filename (str): name of file
        text (str): text to be written to file

    Return:
        returns the number of characters written
    '''
    with open(filename, 'a') as f:
        return f.write(text)
