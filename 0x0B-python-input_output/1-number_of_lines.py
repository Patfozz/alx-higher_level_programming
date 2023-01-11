#!/usr/bin/python3
'''
Defines a function number_of_lines
'''


def number_of_lines(filename=''):
    '''returns the number of lines in a text file

    Args:
        filename (str): the file to open

    Return:
        returns the number of lines
    '''
    with open(filename) as f:
        for i, v in enumerate(f, 1):
            pass
    return i
