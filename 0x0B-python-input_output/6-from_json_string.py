#!/usr/bin/python3
'''
Defines a function from_json_string
'''
import json


def from_json_string(my_str):
    '''returns an object represented by JSON string

    Args:
        my_str (str): JSON string

    Return:
        Returns an object
    '''
    return json.loads(my_str)
