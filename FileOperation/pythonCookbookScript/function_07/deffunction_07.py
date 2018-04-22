#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 20 Apr 2018 04:56:25 PM CST
# File Name: deffunction_07.py
# Description:  回掉内联函数
                    定义一个一个执行某种计算任务然后调用一个回调函数的函数
"""

def apply_async(func, args, callback):
    #Computer the result
    result = func(*args)

    #Invoke the callback with the result
    callback(result)

#A example

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x+y

print(apply_async(add, (2, 3), callback=print_result))
print("--------------------------------------------")
print(apply_async(add,('hello', 'world'), callback=print_result))



