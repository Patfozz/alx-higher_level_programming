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

    def to_json(self):
        '''Retrieves a dictionary representation of instance

        '''
        return self.__dict__
