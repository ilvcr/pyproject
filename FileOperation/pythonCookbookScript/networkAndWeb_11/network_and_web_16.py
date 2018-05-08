#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 06 May 2018 03:44:38 PM CST
# File Name: network_and_web_16.py
# Description:  使用 JSON、 XML 或一些其他的编码格式序列化消息
"""

#将pickle.loads() 和 pickle.dumps() 替换成 json.loads() 和 json.dumps()

#jsonrpcserver.py
import json

class RPCHandler(object):
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                #Receive a message
                func_name, args, kwargs = json.loadds(connection.recv())
                #Run the RPC and send a reponse
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(json.dumps(r))
                except Exception as e:
                    connection.send(json.dumps(str(e))
        except EOFError:
            pass

#jsonrpcclient.py
import json

class RPCProxy(object):
    def __init__(self, connection):
        self._connection = connection
    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(json.dumps((name, args, kwargs)))
            result = json.loads(self._connection.recv())
            return result
        return do_rpc

