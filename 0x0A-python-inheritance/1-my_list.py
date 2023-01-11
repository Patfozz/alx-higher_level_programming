#!/usr/bin/python3
'''
This module defines a class MyList.
'''


class MyList(list):
    '''Custom list class that inherits from list.
    '''

    def print_sorted(self):
        '''Prints a sorted version of the list
        '''
        print(sorted(self)
