#!/usr/bin/python3
'''
Defines read_lines function
'''


def read_lines(filename='', nb_lines=0):
    '''Reads n lines of a text file and prints it to stdout

    Args:
        filename (str): file to be opened
        nb_lines: number of lines to read
    '''
    with open(filename) as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end='')
        else:
            for i, v in enumerate(f, 1):
                if i <= nb_lines:
                    print(v, end='')
                else:
                    break
