#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 11:13:13 PM CST
# File Name: network_and_web_07.py
# Description:  使用StreamRequestHandler 基类将一个类文件接口放置在底层socket 上
"""

from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        #self.rfile is a file-like object for reading
        for line in self.rfile:
            #self.wfile is a file-like object for writing
            self.wfile.write(line)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
