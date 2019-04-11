#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: startthreading.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Fri Apr  5 22:21:46 2019
# Description: 
#************************************************************************#

import time

def countdown(n):
    while n > 0:
        print 'T-minus', n
        n -= 1
        time.sleep(2)

from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start()


if t.is_alive():
    print 'Still runing'
else:
    print 'Complete'





