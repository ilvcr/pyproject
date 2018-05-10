#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 06:26:21 PM CST
# File Name: concurrent_programming_01.py
# Description:  启动与停止线程
                    threading 库可以在单独的线程中执行任何的在 Python 中可以调用的对象
"""

#创建一个 Thread 对象并将要执行的对象以 target 参数的形式提供给该对象

#Code to execute in an independent thread

import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

#Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()

if t.is_alive():
    print("Still running")
else:
    print("Completed")
