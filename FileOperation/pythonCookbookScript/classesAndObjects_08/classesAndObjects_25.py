#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 07:46:05 PM CST
# File Name: classesAndObjects_25.py
# Description:  在类中定义多个构造器
                    实现一个类，除了使用 init () 方法外, 为了实现多个构造器，需要使用到类方法
"""

import time

class Date(object):
    '''方法一：使用类方法'''

    #Primary constructor

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    #Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)
b = Date.today()
