#!/usr/bin/python3
import sys
from os import path
from typing import List
from importlib import import_module

save_to_json_file = import_module("5-save_to_json_file").save_to_json_file
load_from_json_file = import_module("6-load_from_json_file").load_from_json_file

def add_item(filename: str, items: List[str]):
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []
    my_list.extend(items)
    save_to_json_file(my_list, filename)

if __name__ == '__main__':
    filename = 'add_item.json'
    items = sys.argv[1:]
    add_item(filename, items)
