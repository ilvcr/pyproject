#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testiter.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 12:37:59 2019
# Description: 
#************************************************************************#


i = iter("abc")
print i.next()
print '------------------------------'
print i.next()

print '------------------------------'

print i.next()

print '------------------------------'

#print i.next()

print '------------------------------'


class MyIterator(object):
    def __init__(self, step):
        self.step = step
    def next(self):
        '''Return the next element.'''
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        '''Return the iterator itself.'''
        return self


print '------------------------------'

for el in MyIterator(10):
    print el

print '------------------------------'


