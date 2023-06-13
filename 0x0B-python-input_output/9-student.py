#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        attributes = {}
        for attr in dir(self):
            if not attr.startswith('__') and not callable(getattr(self, attr)):
                attributes[attr] = getattr(self, attr)
        return attributes
