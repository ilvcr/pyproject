#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testweakref.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Thu Mar 28 20:02:41 2019
# Description: 
#************************************************************************#

# error


import weakref

s1 = {1, 2, 3}

s2 = s1

def bye():
    print 'Gone with the wind...'

ender = weakref.finalize(s1, bye)

print '----------------------------------------------\n\n'
print ender.alive
print '\n\n----------------------------------------------'

del s1

print ender.alive


