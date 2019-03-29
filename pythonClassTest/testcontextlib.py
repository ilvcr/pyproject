#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testcontextlib.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:59:10 2019
# Description: 
#************************************************************************#


from contextlib import contextmanager
from __future__ import with_statement

@contextmanager
def context():
    print 'entering the zone'
    try:
        yield
    except Exception as e:
        print 'with an error {}'.format(e)
        raise e
    else:
        print 'with no error'















