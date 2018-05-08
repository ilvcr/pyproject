#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 05 May 2018 10:57:51 PM CST
# File Name: network_and_web_10.py
# Description:  创建 UDP 服务器
                    实现一个基于 UDP 协议的服务器来与客户端通信
"""


#简单的时间服务器

from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandle(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        #Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serv_forever()
