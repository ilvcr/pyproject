#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 06 May 2018 03:54:29 PM CST
# File Name: network_and_web_17.py
# Description:  简单的客户端认证
                    在分布式系统中实现一个简单的客户端连接认证功能，又不想像 SSL 那样的复杂
"""

#利用 hmac 模块实现一个连接握手，从而实现一个简单而高效的认证过程
imprt hmac
import os

def client_authenticate(connection, secret_key):
    '''
    Authenticate client to a remote service.
    connection represents a network connection.
    secret_key is a key known only to both client/server.
    '''

    message = connection.recv(32)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    connection.send(digest)


def server_authenticate(connection, secret_key):
    '''
    Request client authentication.
    '''

    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest, response)
