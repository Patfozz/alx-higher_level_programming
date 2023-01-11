#!/usr/bin/python3
'''
Defines load_from_json_file function
'''
import json


def load_from_json_file(filename):
    '''Creates an object from a "JSON file"

    Args:
    my_obj (obj): object to be written to file
    filename (str): file to write to
    '''
    with open(filename, 'r') as f:
        return json.loads(f.read())
