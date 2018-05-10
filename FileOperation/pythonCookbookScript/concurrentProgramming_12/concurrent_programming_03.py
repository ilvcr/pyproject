#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 06:46:22 PM CST
# File Name: concurrent_programming_03.py
# Description:  利用超时循环来小心操作线程
"""

class IOTask(object):
    def terminate(self):
        self._running = False

    def run(self, sock):
        #sock is a socket
        sock.settimeout(5)  #Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except sock.timeout:
                continue
            # Continued processing
            # ...
        # Terminated
        return
