#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 09 May 2018 09:32:17 PM CST
# File Name: concurrent_programming_15.py
# Description:  concurrent.futures 函数库有一个 ThreadPoolExecutor 类
"""

#简单的 TCP 服务器，使用一个线程池来响应客户端

from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock, client_addr):
    '''
    Handle a client connection
    '''
    print('Got connection from',client_addr)

    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.senfall(msg)
    print('Client closed connection')
    sock.closed()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = sock(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


echo_server(('', 15000))
