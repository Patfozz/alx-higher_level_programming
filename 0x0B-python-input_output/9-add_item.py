#!/usr/bin/python3
'''
Adds all arguments to a Python list and then saves them to a file
'''
import sys


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = 'add_item.json'

try:
    file_list = load_from_json_file(filename)
except BaseException:
    file_list = []
for i in sys.argv[1:]:
    file_list.append(i)
save_to_json_file(file_list, filename)
