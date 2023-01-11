#!/usr/bin/python3
'''
Defines save_to_json_file function
'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an object to a text filename

    Args:
    my_obj (obj): object to be written to file
    filename (str): file to write to
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
