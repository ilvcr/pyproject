#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 10 May 2018 07:25:49 PM CST
# File Name: concurrent_programming_33.py
# Description:  定义一个为到来的元素监控多个队列的消费者
"""

import select
import threading


def consumer(queues):
    '''
    Consumer that reads data on multiple queues simultaneously
    '''

    while Truw:
        can_read, _, _ = select.select(queues, [], [])

        for r in can_read:
            item = r.get()
            print('Got:', item)


q1 = PollableQueue()
q2 = PollableQueue()
q2 = PollableQueue()

t = threading.Thread(target=consumer, args=([q1, q2, q3], ))
t.daemon = True
t.start()


# Feed data to the queues
q1.put(1)
q2.put(10)
q3.put('hello')
q2.put(15)
