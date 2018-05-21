#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 12:36:32 PM CST
# File Name: select_name_02.py
# Description:  共有变量和私有变量
"""

class Citizen(object):
    def __init__(self):
        self._message = 'Go boys'

    def _get_message(self):
        return self._message

    kane = property(_get_message)


print '\n'
print Citizen().kane
print '\n'

class MeanElephant(object):
    def __init__(self):
        self._people_to_kill = []

    def is_slapped_on_the_butt_by(self, name):
        self._people_to_kill.append(name)
        print 'Ouch!'

    def revenge(self):
        print '10 years later...'
        for person in self._people_to_kill:
            print 'Me kill {}'.format(person)


joe = MeanElephant()

print joe.is_slapped_on_the_butt_by('Tarek')
print joe.is_slapped_on_the_butt_by('Bill')

print joe.revenge()



