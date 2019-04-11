#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testproperty.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 21:48:55 2019
# Description: 
#************************************************************************#

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(slef, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function(options)
    @first_name.deleter
    def first_name(slef):
        raise AttributeError("Can't delete attribute")

a = Person("Guido")
print a.first_name
print "\n==================\n"
a.first_name = 42
del a.first_name

print "\n==================\n"






