#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Mon 16 Apr 2018 05:59:47 PM CST
# File Name: deffunction_02.py
# Description:  代码功能: 实现一个简单的echo服务器

"""

from socketserver import StreamRequestHandler, TCPServer
from functools import partial


class EchoHandler(StreamRequestHandler):
    #ack is added keyword-only argument. *args, **kwargs are
    #any normal parameters supplied (which are passed on)

    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
                self.wfile.write(self.ack + line)


if __name__ == "__main__":
    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    serv.serve_forever()
