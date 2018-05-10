#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 10:48:09 PM CST
# File Name: concurrent_programming_21.py
# Description:  结合使用一个线程和一个队列定义 actor
"""

from queue import Queue
from threading import Thread, Event

#Sentinel used for shutdown
class ActorExit(Exception):
    pass


class Actor(object):
    def __init__(self):
        self._mailbox = Queue()


    def send(self, msg):
        '''
        Send a message to the actor
        '''
        self._mailbox.put(msg)


    def recv(self):
        '''
        Receive an incoming message
        '''
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()

        return msg


    def close(self):
        '''
        Close the actor, thus shutting it down
        '''
        self.send(ActorExit)


    def start(self):
        '''
        Start concurrent execution
        '''
        self._terminated = Even()
        t = Thread(target=self._bootstrap)

        t.daemon = True
        t.start()


    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()


    def join(self):
        self._terminated.wait()


    def run(self):
        '''
        Run method to be implemented by the user
        '''
        while True:
            msg = self.recv()


#Sample ActorTask
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got:', msg)


#Sample use
p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()

