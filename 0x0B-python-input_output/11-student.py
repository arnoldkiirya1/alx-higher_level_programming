#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if attrs is None:
            attrs = [attr for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr))]
        else:
            attrs = [attr for attr in attrs if hasattr(self, attr)]
        
        return {attr: getattr(self, attr) for attr in attrs}
    
    def reload_from_json(self, json):
        for attr, value in json.items():
            setattr(self, attr, value)
