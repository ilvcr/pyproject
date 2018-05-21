#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 16 May 2018 02:14:31 PM CST
# File Name: best_implemt_grammer_18.py
# Description:  创建一个上下文，以装备指定类的所有公共API
"""

import logging
from __future__ import with_statement
from contextlib import contextmanager

@contextmanager
def logger(klass, logger):
    #记录器
    def _log(f):
        def __log(*args, **kwargs):
            logger(f, args, kwargs)
            return f(*args, **kwargs)

        return __log

    #装备该类
    for attribute in dir(klass):
        if attribute.startswith('_'):
            continue
        element = getattr(klass, attribute)
        setattr(klass, '__loged_%s' % attribute, element)
        setattr(klass, attribute, _log(element))


        #正常工作
    yield klass


    for attribute in dir(klass):
        if not attribute.startswith('__loged_'):
            continue
        element = getattr(klass, attribute)
        setattr(klass, attribute[len('__loged_'):], element)

        delattr(klass, attribute)


