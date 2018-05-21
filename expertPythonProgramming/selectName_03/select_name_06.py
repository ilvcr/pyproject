#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 17 May 2018 01:02:16 PM CST
# File Name: select_name_06.py
# Description:  *args和**kwargs的使用
"""

def fuzzy_thing(**kwargs):
    if 'do_this' in kwargs:
        print 'ok i did'

    if 'do_that' in kwargs:
        print 'that is done'

    print 'errr... ok'


print fuzzy_thing()

print fuzzy_thing(do_this=1)

print fuzzy_thing(do_that=1)

print fuzzy_thing(hahahahahahah=1)



