#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 15 May 2018 01:57:41 PM CST
# File Name: best_implemt_grammer_09.py
# Description:  multitask包为套接字处理(echo服务器)提供的API
"""

from __future__ import with_statement
from contextlib import closing
import socket
import multitask

def client_handler(sock):
    with closing(sock):
        while True:
            data = (yield multitask.recv(sock, 1024))
            if not data:
                break

            yield multitask.send(sock, data)


def echo_server(hostname, port):
    addrinfo = socket.getaddrinfo(hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM)

    (family, socktype, proto, canonname, sockaddr) = addrinfo[0]

    with closing(socket.socket(family,
                                socktype,
                                proto)) as sock:

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(sockaddr)
        sock.listeen(5)
        while True:
            multitask.add(client_handler((yield multitask.accept(sock))[0]))


if __name__ == '__main__':
    import sys

    hostname = None
    port = 1111
    if len(sys.argv) > 1:
        hostname = sys.argv[1]

    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    multitask.add(echo_server(hostname, port))

    try:
        multitask.run()
    except KeyboardInterrupt:
        pass


