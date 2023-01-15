#!/usr/bin/python3
'''
Defines a class Base
'''
import json
import csv
import os


class Base:
    '''Base of all other classes in this project

    goal is to manage id attribute in all future classes

    Attributes:
        __nb_objects (int): number of Base objects created
        id (int): the id of the object
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes a Base object

        Args:
            id (int): the id of the Base object
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries ([[]]): a list of dictionaries

        Return:
            returns the JSON representation of list_dictionaries or \
            "[]" if list_dictionaries is None or empty
        '''
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the JSON string representation

        Args:
            json_string (str): the JSON string

        Return:
            returns a list of JSON strings
        '''
        return json.loads(json_string or '[]')

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all atrributes setattr

        Args:
            dictionary (**dict): double pointer to a dictionary

        Returns:
            instance with all attributes set
        '''
        if cls.__name__ == 'Rectangle':
            new = cls(1, 1)
        if cls.__name__ == 'Square':
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances
        '''
        try:
            json_string = cls.to_json_string(
                [x.to_dictionary() for x in list_objs])
        except BaseException:
            json_string = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances

        Return:
            returns a list of instances form a JSON string
        '''
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                list_dict = cls.from_json_string(f.read())
            return ([cls.create(**x) for x in list_dict])
        except FileNotFoundError:
            return ([])
