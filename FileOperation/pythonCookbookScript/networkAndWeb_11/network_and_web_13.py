#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 05 May 2018 11:50:07 PM CST
# File Name: network_and_web_13.py
# Description:  通过 XML-RPC 实现简单的远程调用
                    找到一个简单的方式去执行运行在远程机器上面的 Python 程序中的函数或方法。
"""

#使用 XML-RPC实现一个最简单远程方法调用。实现一个实现了键 -值存储功能的简单服务器：

from xmlrpc.server import SimpleXMLRPCServer

class KeyValueServer(object):
    _rpc_methods = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self.data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods:
            self._serv.register_function(getattr(self, name))


    def get(self, name):
        return self._data[name]

    def set(self, naem, value):
        self._data[naem] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def server_forever(self):
        self._serv.server_forever()


#Example
if __name__ == '__main__':
    kvserv = KeyValueServer(('', 15000))
    kvserv.serve_forever()
