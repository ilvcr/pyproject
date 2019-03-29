#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testinit_01.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Mar 28 18:24:16 2019
# Description: 
#************************************************************************#

class Gizmo:
    def __init__(self):
        print 'Gizmo id: {}'.format(id(self))


x = Gizmo()
print x

print '-------------------------'

print dir()

print '-------------------------'

'''
y = Gizmo() * 10
print y
'''
#print dir()
