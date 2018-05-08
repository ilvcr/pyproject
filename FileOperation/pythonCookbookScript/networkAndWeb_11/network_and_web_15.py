#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 06 May 2018 12:09:35 AM CST
# File Name: network_and_web_15.py
# Description:  实现远程方法调用
                    在一个消息传输层如 sockets 、 multiprocessing connections 或 ZeroMQ 的
                    基础之上实现一个简单的远程过程调用（RPC）

            将函数请求、参数和返回值使用 pickle 编码后，在不同的解释器直接传送 pickle 字节字符串，
                可以很容易的实现 RPC
"""

#简单的 PRC 处理器被整合到一个服务器中

#rpcserver.py

import pickle

class RPCHandler(object):
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func


    def handle_connection(self, connection):
        try:
            while True:
                #Receive a message
                func_name, args, kwargs = pickle.loads(connection.recv())
                #Run the RPC and send a response
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e)))

        except EOFError:
            pass


#RPC 服务器
from multiprocessing.connection import Listener
from threrading import Thread

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.deamon = True
        t.start()

# Some remote functions
def add(x, y):
    return x+y

def sub(x, y):
    return x-y

# Register with a handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

# Run the server
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')


#从一个远程客户端访问服务器，需要创建一个对应的用来传送请求的 RPC代理类
import pickle

    class RPCProxy(object)::
        def __init__(self, connection):
            self._connection = connection

        def __getattr__(self, name):
            def do_rpc(*args, **kwargs):
                self._connection.send(pickle.dumps((name, args, kwargs)))
                result = pickle.loads(self._connection.recv())
                if isinstance(result, Exception):
                    raise result
                return result
            return do_rpc
