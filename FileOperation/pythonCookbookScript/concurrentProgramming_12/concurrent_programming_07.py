#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 07:46:44 PM CST
# File Name: concurrent_programming_07.py
# Description:  使用信号量唤醒单个线程
"""

#Worker thread
def work(n, sema):
    #Wait to be signaled
    sema.acquire()

    #Do some work
    print('Working', n)


#Creat some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=work, args=(n, sema, ))
    t.start()
