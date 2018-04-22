#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 21 Apr 2018 05:38:34 PM CST
# File Name: classesAndObjects_03.py
# Description:   让对象支持上下文管理协议(with语句)
                    让对象兼容with语句, 选哟实现__enter__()和__exit__()方法
"""

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection(object):

    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None


    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock  = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exy_ty, exy_val, tb):
        self.sock.close()
        self.sock = None
