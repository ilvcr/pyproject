#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testenterandexit.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:51:51 2019
# Description: 
#************************************************************************#

class Context(object):
    def __enter__(self):
        print 'Enter tne zone'
    def __exit__(slef, exception_type, exception_value, exception_traceback):
        print 'leaving the zone'
        if exception_type is None:
            print 'with no error'
        else:
            print 'with an error {}'.format(exception_value)

print '------------------------------'
with Context():
    print 'i am the zone'

print '------------------------------'
with Context():
    print 'i am the buggy zone'
    raise TypeError('i am the bug')
    

print '------------------------------'



print '------------------------------'







