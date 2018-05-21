#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 12:46:07 PM CST
# File Name: select_name_04.py
# Description:  属性名称
"""

class Connection(object):
    _connected = []

    def connect(self, user):
        self._connected.append(user)

    def _connected_people(self):
        return '\n'.join(self._connected)

    connected_people = property(_connected_people)


my = Connection()
my.connect('Tarek')
my.connect('Shannon')

print my.connected_people


