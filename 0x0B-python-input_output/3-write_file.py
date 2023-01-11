#!/usr/bin/python3
'''
defines write_file function
'''


def write_file(filename='', text=''):
    '''writes a string to a text file

    Args:
        filename (str): name of file
        text (str): text to be written to file

    Return:
        returns the number of characters written
    '''
    with open(filename, 'w') as f:
        return f.write(text)
