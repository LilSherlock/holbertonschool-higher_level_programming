#!/usr/bin/python3
""" students class """


class Student():
    """ class student """

    def __init__(self, first_name, last_name, age):
        """init function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json function"""
        if not isinstance(attrs, list):
            return self.__dict__
        for element in attrs:
            if not isinstance(element, str):
                return self.__dict__
        return {key: value for (key, value)
                in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """ reload from json function """
        for k, v in json.items():
            self.__dict__[k] = v
