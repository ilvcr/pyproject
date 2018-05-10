#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 11:00:36 PM CST
# File Name: concurrent_programming_22.py
# Description:  类 actor 对象通过生成器来简化定义
"""

def print_actor():
    while True:
        try:
            msg = yield   #Get a message
            print('Got:', msg)
        except GeneratorExit:
            print('Actor terminationg')



#Sample use
p = print_actor()
next(p)
p.send('Hello')  #Address to thr yield (ready to recvieve)
p.send('World')
p.close()

