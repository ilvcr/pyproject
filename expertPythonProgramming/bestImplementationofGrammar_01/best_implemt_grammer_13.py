#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 02:28:31 PM CST
# File Name: best_implemt_grammer_13.py
# Description:  编写自定义装饰器的通用模式：
                    编写一个函数，返回封装原始函数调用的一个子函数
"""

def mydecorator(function):
    def _mydecorator(*args, **kwargs):
        #在调用实际函数之前做些填充工作
        res = function(*args, **kwargs)
        #做完填充工作后
        return res

    #返回子函数
    return _mydecorator


#装饰器需要参数时的情况
#需要二级封装
def Mydecorator(arg1, arg2):
    def _Mydecorator(function):
        def __Mydectorator(*args, **kwargs):
            #在调用实际函数之前做些填充工作
            res = function(*args, **kwargs)
            #做完填充工作后
            return res

        #返回子函数
        return __Mydectorator
    return _mydecorator

