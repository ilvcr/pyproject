#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 06 May 2018 04:01:56 PM CST
# File Name: network_and_web_18.py
# Description:   sockets服务器代码
"""

from socket import socket, AF_INET, SOCK_STREAM

secret_key = b'peekabo'
def echo_handler(client_sock):
    if not server_authentocate(client_sock, secret_key):
        client_sock.close()
        return

    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    while True:
        c, a = s.accept()
        echo_handler(c)

echo_server(('', 18000))



#Within a client, you would do this:
from socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
s.send(b'Hello World')
resp = s.recv(1024)
