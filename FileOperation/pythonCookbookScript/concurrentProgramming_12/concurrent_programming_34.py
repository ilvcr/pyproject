#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 10 May 2018 07:31:35 PM CST
# File Name: concurrent_programming_34.py
# Description:  同时轮询套接字和队列
"""

import select

def event_loop(sockets, queues):
    while True:
        # polling with a timeout
        can_read, _, _ = select.select(sockets, [], [], 0.01)

        for r in can_read:
            handle_read(r)

        for q in queues:
            if not q.empty():
                item = q.get()
                print('Got:', item)
