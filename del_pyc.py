#! /usr/bin/python
# coding:utf8

__author__ = 'fei'


import os
import shutil

dir_path = os.path.dirname(__file__)

def del_pyc(path):
    for dir_name, sub_dir_name, file_names in os.walk(path):
        for file_name in file_names:
            if file_name.endswith('.pyc'):
                file_name = os.path.join(dir_name, file_name)
                if os.path.isfile(file_name):
                    os.remove(file_name)

if __name__ == "__main__":
    del_pyc(dir_path)