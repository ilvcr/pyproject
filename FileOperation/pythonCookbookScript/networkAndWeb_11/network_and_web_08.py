#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 11:52:11 PM CST
# File Name: network_and_web_08.py
# Description:  StreamRequestHandler 通过设置其他的类变量来支持一些新特性
"""

import socket

class EchoHandler(StreamRequestHandler):
    #Optional setting (defaults shown)
    timeout = 5                         #Timeout on all socket operational
    rbufsize = -1                       #Read buffer size
    wbufsize = 0                        #Write buffer size
    disable_nagle_algorithm = False     #Sets TCP_NODELAY socket optional

    def handle(self):
        print('Got connectional from', self.client_address)
        try:
            for line in self.rfile:
                #self.wfile is a file-like object for writing
                self.wfile.write(line)

        except socket.timeout:
            print('TIme out!')
