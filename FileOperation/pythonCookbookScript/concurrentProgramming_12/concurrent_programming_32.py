#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Thu 10 May 2018 07:05:14 PM CST
# File Name: concurrent_programming_32.py
# Description:  多个线程队列轮询
"""

#对于每个想要轮询的队列创建一对连接的套接字。
'''
在其中一个套接字上面编写代码来标识存在的数据，
另外一个套接字被传给 select() 或类似的一个轮询数据到达的函数
'''

import queue
import socket
import os


class PollableQueue(queue.Queue):
    def __init__(self):
        super().__init__()
        # Create a pair of connected sockets
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # Compatibility on non-POSIX systems
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)

            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()


    def fileno(self):
        return self._getsocket.fileno()


    def put(self, item):
        super().put(item)
        self._putsocket.send(b'x')


    def get(self):
        self._getsocket.recv(1)
        return super().get()



