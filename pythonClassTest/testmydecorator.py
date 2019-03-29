#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: testmydecorator.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Mar 29 13:15:28 2019
# Description: 
#************************************************************************#



#通用模板
def mydecorator(function):
    def _mydecorator(*args, **kwargs):
        res = function(*args, **kwargs)
        return res
    return _mydecorator


#带参数的模板
def mydecorator2(arg1, arg2):
    def _mydecorator(function):
        def __mydecorator(*args, **kwargs):
            res = function(*args, **kwargs)
            return res
        return __mydecorator
    return _mydecorator


















