#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testlogging.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 14:02:05 2019
# Description: 
#************************************************************************#

import logging
from __future__ import with_statement
from contextlib import contextmanager

@contextmanager
def logged(klass, logger):
    # 记录器
    def _log(f):
        def __log(*args, **kw):
            logger(f, args, kw)
            return f(*args, **kw)
        return __log

    #装备该类
    for attribute in dir(klass):
        if attribute.startswith('_'):
            continue
        element = getattr(klass, attribute)
        setattr(klass, '__logged_{}'.format(attribute), element)
        setattr(klass, attribute, _log(element))

    yield klass

    for attribute in dir (klass):
        if not attribute.startswith('__logged_'):
            continue
        element = getattr(klass, attribute)
        setattr(klass, attribute[len('__logged_'):], element)
        delattr(klass, attribute)


class One(object):
    def _private(self):
        pass
    def one(self, other):
        self.two()
        other.thing(self)
        self._private()
    def two(self):
        pass


class Two(object):
    def thing(self, other):
        other.two()

calls = []

def calles(meth, args, kw):
    calls.append(meth.im_func.func_name)

with logged(One, called):
    one = One()
    two = Two()
    one.one(two)

print calls










