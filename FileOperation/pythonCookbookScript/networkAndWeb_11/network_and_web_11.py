#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sat 05 May 2018 11:10:00 PM CST
# File Name: network_and_web_11.py
# Description:  例化一个 ForkingUDPServer 或 ThreadingUDPServer 对象实现并发操作
"""

from socketserver import ThreadingUDPServer

if __name__ == '__main__':
    serv = ThreadingUDPServer(('', 20000), TimeHanddler)
    serv.serve_forever()


#直接使用 socket 构造一个 UDP 服务器
from socket import socket, AF_INET, SOCK_DGRAM
import time


def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


if __name__ == '__main__':
    time_server(('', 20000))
