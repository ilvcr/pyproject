#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 06 May 2018 04:10:23 PM CST
# File Name: network_and_web_19.py
# Description:  在网络服务中加入 SSL
                    实现一个基于 sockets 的网络服务，客户端和服务器通过 SSL 协议认证并加密传输的数据
"""

#一个简单的应答服务器，能在服务器端为所有客户端连接做认证

from socket import socket, AF_INET, SOCK_STREAM
import ssl

KEYFILE = 'server_key.pem' # Private key of the server
CERTFILE = 'server_cert.pem' # Server certificate (given to client)

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('COnnection closed')


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    #Wrap with an SSL layer requiring client certs
    s_ssl = ss1.wrap_socket(s,
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            server_side=True
                            )

    #Wait for connections
    while True:
        try:
            c, a = s_ssl.accept()
            print('Got connection', c, a)
            echo_client(c)
        except Exception as e:
            print('{} : {}'.format(e.__class__.__name__, e))


echo_server(('', 20000))
