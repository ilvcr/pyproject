#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 06:36:44 PM CST
# File Name: concurrent_programming_09.py
# Description:  task done() 和 join()提供一些基本完成的特性
"""

from queue import Queue
from threading import Thread

#A thread that produces data
def producer(out_q):
    while running:
        #Produce some data
        #...
        out_q.put(data)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Process the data
        #...
        # Indicate completion
        in_q.task_done()


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

#Wait for all produced items to be consumed
q.join()


