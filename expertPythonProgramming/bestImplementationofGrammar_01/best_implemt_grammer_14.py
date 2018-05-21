#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 02:36:28 PM CST
# File Name: best_implemt_grammer_14.py
# Description:  常见的装饰器模式：  参数检查
"""

#提供确保输入输出与签名有关的类型

from itertools import izip

rpc_info = {}


#装饰器将函数注册到全局字典中，并将其作为其参数和返回值保存在一个列表类型
def xmlrpc(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        #注册签名
        func_name = function.func_name

        rpc_info[func_name] = (in_, out)

        def _check_types(elements, types):
            '''Subfunction that checks the types.'''
            if len(elements) != len(types):
                raise TypeError('argument count is wrong')

            typed = enumerate(izip(elements, types))

            for index, couple in typed:
                arg, of_the_right_type = couple

                if isinstance(arg, of_the_right_type):
                    continue

                raise TypeError('arg #{1} should be {2}'.format(index, of_the_right_type))

        #封装函数
        def __xmlrpc(*args):        #没有允许的关键字
            #检查输入的内容
            checkable_args = args[1:]  #removing self
            _check_types(checkable_args, in_)

            #执行该函数
            res = function(*args)

            #检查输入内容
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)

            #函数类型检查成功
            return res

        return __xmlrpc
    return _xmlrpc


#USE
class RPCView(object):
    @xmlrpc((int, int))  #two int -> None
    def meth1(self, int1, int2):
        print 'received {} and {}'.format(int1, int2)


    @xmlrpc((str,), (int,))  #string -> int
    def meth2(self, phrase):
        print 'received {}'.format(phrase)
        return 12


print rpc_info

my = RPCView()

print my.meth1(1, 2)
print my.meth2(2)


