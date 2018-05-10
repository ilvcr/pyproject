#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 11:23:29 PM CST
# File Name: concurrent_programming_27.py
# Description:  一个简单的诊断类显示被发送的消息
"""

class DisplayMessage(object):
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))


exc = get_exchange('name')
d = DisplayMessage()
exc.attach(d)


