#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 07:02:06 PM CST
# File Name: concurrent_programming_13.py
# Description:  对定义的LazyConnection 上下文管理器类进行一些小的修改使得可以适用于多线程
"""

from socket import socket, AF_INET, SOCK_STREAM
import threading

class LazyConnection(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()


    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock


    def __exit__(self, exc_ty, exc_val, tb):
        self.local.sock.close()
        del self.local.sock


