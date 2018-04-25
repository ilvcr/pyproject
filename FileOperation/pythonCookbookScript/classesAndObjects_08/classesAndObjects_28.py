#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 25 Apr 2018 08:26:00 PM CST
# File Name: classesAndObjects_28.py
# Description:  实现状态对象或者状态机

                    实现一个状态机或者是在不同状态下执行操作的对象，但又不想在代码中出现太多的条件判断语句。
"""

class Connection(object):
    '''
    普通方案，好多个判断语句，效率低下 ~~
    '''

    def __init__(self):
        self.state = 'CLOSED'


    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')


    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('writing')


    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'


    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'


class ConnectionNew(object):
    '''
    新方案——对每个状态定义一个类
    '''

    def __init__(self):
        self.new_state(ClosedConnectionState)


    def new_state(self, newstate):
        self._state = newstate
        #Delegate to the state class


    def read(self):
        return self._state.read(self)


    def write(self, data):
        return self._state.write(self, data)


    def open(self):
        return self._state.open(self)


    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState(object):
    @staticmethod
    def read(conn):
        raise NotImplementedError()


    @staticmethod
    def write(conn, data):
        raise NotImplementedError()


    @staticmethod
    def open(cnn):
        raise NotImplementedError()


    @staticmethod
    def close(cnn):
        raise NotImplementedError()


#Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(cnn):
        raise RuntimeError('Not open')


    @staticmethod
    def write(cnn, data):
        raise RuntimeError('Not open')


    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)


    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')



class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')


    @staticmethod
    def write(conn, data):
        print('writing')


    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')


    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)
