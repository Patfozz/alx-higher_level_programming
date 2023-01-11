#!/usr/bin/python3
'''
Defines a class Student
'''


class Student:
    '''Student class


    '''

    def __init__(self, first_name, last_name, age):
        '''Initializes a Student object

        Attributes:
            first_name (str): first name of Student
            last_name (str): last name of Student
            age (int): age of Student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation of instance

        '''
        if attrs and \
           isinstance(attrs, list) is True and\
           all(isinstance(x, str) for x in attrs) is True:
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance

        Args:
        json (dict): the dictionary
        '''
        self.__dict__ = json
