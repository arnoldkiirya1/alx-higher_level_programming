#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split(", ")[-1].replace(" language", "") + " with Python"
print(str)
