#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 02:42:41 PM CST
# File Name: best_implemt_class_03.py
# Description:  继承中的问题
"""

class Mamma(object):    #old method
    def says(self):
        print 'do your homework!'


class Sister(Mamma):
    def says (self):
        Mamma.says(self)
        print 'and yclean your bedroom'

antia = Sister()
print antia.says()


class Brother(Mamma):       #new method
    def says(self):
        super(Brother, self).says()
        print 'and clean your cloth'

bib = Brother()
print bib.says()


