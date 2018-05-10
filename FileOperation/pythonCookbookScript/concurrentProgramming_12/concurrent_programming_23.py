#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 11:05:01 PM CST
# File Name: concurrent_programming_23.py
# Description:  以元组形式传递标签消息让 actor 执行不同的操作
"""

class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_'+tag)(*payload)


    # Methods correponding to different message tags
    def do_A(self, x):
        print('Running A', x)


    def do_B(self, x, y):
        print('Running B', x, y)



#Example
a = TaggedActor()
a.start()
a.send(('A', 1))  #Invokes do_A(1)
a.send(('B', 2, 3))  #Invokes do_B(2, 3)


