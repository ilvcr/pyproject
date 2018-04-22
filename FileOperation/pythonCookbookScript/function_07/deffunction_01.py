#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 05:43:26 PM CST
# File Name: deffunction_01.py
# Description:
                partial()通常被用来微调其他库函数所使用的回调函数的参数。

                代码功能: 使用multiprocessing来异步计算一个结果值, 然后这个值
                          被传递给一节接受一个result值和一个可选的logging参数
                          的回调函数
"""

def output_result(result, log=None):
    if log is not None:
        log.debug("Got: %r",result)

#A sample function
def add(x, y):
    return x + y
if __name__ == '__main__':

    import  logging as lg
    from multiprocessing import Pool as pl
    from functools import partial as pt

    lg.basicConfig(level=lg.DEBUG)
    log = lg.getLogger('test')

    p = pl()
    p.apply_async(add, (3, 4), callback=pt(output_result, log=log))
    p.close()
    p.join()

'''
当给 apply async() 提供回调函数时，通过使用 partial() 传递额外的 logging
参数。而 multiprocessing 仅仅只是使用单个值来调用回调函数。
'''
