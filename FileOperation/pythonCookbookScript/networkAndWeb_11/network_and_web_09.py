#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 04 May 2018 11:59:07 PM CST
# File Name: network_and_web_09.py
# Description:  使用socket 直接编程实现的一个服务器
"""

from socket import socket, AF_INET, SOCK_STREAM

def echo_handle(address, client_sock):
    print('Got connection from {}'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handle(client_addr, client_sock)


if __name__ == '__main__':
        echo_server(('', 20000))
