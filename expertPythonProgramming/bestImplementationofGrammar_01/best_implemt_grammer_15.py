#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 03:02:18 PM CST
# File Name: best_implemt_grammer_15.py
# Description:  缓存装饰器
"""

import time
import hashlib
import pickle
from itertools import chain

cache = {}

def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kwargs):
    key = pickle.dumps((function.func_name, args, kwargs))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kwargs):
            key = compute_key(function, args, kwargs)

            #是否已经拥有它了？
            if(key in cache and not is_obsolete(cache[key], duration)):
                print 'we got a winner'
                return cache[key]['value']


            #计算
            result = function(*args, **kwargs)

            #保存结果
            cache[key] = {'value':result, 'time':time.time()}

            return result

        return __memoize

    return _memoize


@memoize()
def very_very_very_complex_stuff(a, b):
    return a + b

print very_very_very_complex_stuff(2, 2)


