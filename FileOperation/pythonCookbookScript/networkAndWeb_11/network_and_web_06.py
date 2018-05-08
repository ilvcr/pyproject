#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 11:03:30 PM CST
# File Name: network_and_web_06.py
# Description:  创建TCP服务器
                    创建一个TCP 服务器的一个简单方法是使用socketserver 库
"""


#一个简单的应答服务器

from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__ = '__main__':
    serv = TcpServer(('', 20000),EchoHandler)
    serv.serve_forever()
