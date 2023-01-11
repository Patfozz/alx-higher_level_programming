#!/usr/bin/python3
'''
Defines read_file function
'''


def read_file(filename=''):
    '''Reads a file and prints it to stdout

    Args:
        filename (str): the filename
    '''
    with open(filename) as f:
        for line in f:
            print(line, end='')
