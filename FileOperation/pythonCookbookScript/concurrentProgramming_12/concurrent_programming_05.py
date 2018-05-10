#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 06:57:25 PM CST
# File Name: concurrent_programming_05.py
# Description:  使用 Event 来协调线程的启动
"""

from threading import Thread, Event
import time

#Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)


#Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

#Wait for the thread to start
started_evt.wait()
print('countdown is running')

