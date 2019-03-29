#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testbus.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Mar 28 18:33:02 2019
# Description: 
#************************************************************************#

import copy

class Bus:
    def __init__(self, passagers=None):
        if passagers is None:
            self.passagers = []
        else:
            self.passagers = list(passagers)

    def pick(self, name):
        self.passagers.append(name)
    
    def drop(self, name):
        self.passagers.remove(name)

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print " Bus1id:{},\n Bus2id:{},\n Bus3id:{}\n".format(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print bus2.passagers

print


print " Bus1id:{},\n Bus2id:{},\n Bus3id:{}\n".format(id(bus1), id(bus2), id(bus3))

print bus3.passagers

