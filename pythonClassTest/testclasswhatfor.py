#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testclasswhatfor.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:09:22 2019
# Description: 
#************************************************************************#


class WhatFor1(object):
    def it(cls):
        print 'work with {}'.format(cls)
    it = classmethod(it)
    def uncommon():
        print 'I could be a global function'
    uncommon = staticmethod(uncommon)


class WhatFor(object):
    @classmethod
    def it(cls):
        print 'work with {}'.format(cls)
    @staticmethod
    def uncommon():
        print 'I could be a global function'

this_is = WhatFor()
print '--------------------------'
print this_is.it()
print '---------------------------'
print this_is.uncommon()


