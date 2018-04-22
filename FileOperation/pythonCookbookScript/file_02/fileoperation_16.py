#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Wed 18 Apr 2018 08:40:06 PM CST
# File Name: fileoperation_16.py
# Description:  使用包装文件描述符的技术将一个类文件接口作用于一个不同方式打开的I/O通道上，
                    如管道, 套接字等
"""

from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):  #客户端
    print("Got connection from",addr)

    #Make texr-mode file wrappers for socket reading/writing
    client_in = open(client_socket.fileno(), 'rt', encoding='latin-1', closed=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closed=False)

    #Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()

def echo_sever(address):  #服务器
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

