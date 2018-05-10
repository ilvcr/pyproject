#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 11:40:34 PM CST
# File Name: concurrent_programming_30.py
# Description: 使用生成器来实现一个不依赖线程的 actor
"""

from collections import deque

class ActorScheduler(object):
    def __init__(self):
        self._actors = {}   # Mapping of names to actors
        self._msg_queue = deque()  # Message queue

    def new_actor(self, name, actor):
        '''
        Admit a newly started actor to the scheduler and give it a name
        '''
        self._msg_queue.append(actor, None)
        self._actors[name] = actor



    def send(self, name, msg):
        '''
        Send a message to a named actor
        '''
        actor = self._actor.get(name)
        if actor:
            self._msg_queue.append(sctor, msg)


    def run(self):
        '''
        Run as long as there are pending messages.
        '''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


#Example use

if __name__ == '__mian__':
    def printer():
        while True:
            msg = yield
            print('Got:', msg)


    def counter(sched):
        while True:
            # Receive the current count
            n = yield
            if n == 0:
                break

            # Send to the printer task
            sched.send('printer', n)
            # Send the next count to the counter task (recursive)

            sched.send('counter', n-1)


    sched = ActorScheduler()
    # Create the initial actors
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    # Send an initial message to the counter to initiate
    sched.send('counter', 10000)
    sched.run()



