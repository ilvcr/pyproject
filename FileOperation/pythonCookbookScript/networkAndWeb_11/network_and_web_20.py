#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 06 May 2018 04:20:04 PM CST
# File Name: network_and_web_20.py
# Description:   对于服务器可以使用一个 mixin 类来添加 SSL
"""

import ssl

class SSLMixin(object):
    '''
    Mixin class that adds support for SSL to existing servers based
    on the socketserver module.
    '''
    def __init__(self, *args, keyfile=None, certfile=None, ca_certs=None, cert_reqs=ssl.NONE, **kwargs):
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)


    def get_request(self):
        client, addr = super().get_request()
        client_ssl = ssl.wrap_socket(client,
        keyfile = self._keyfile,
        certfile = self._certfile,
        ca_certs = self._ca_certs,
        cert_reqs = self._cert_reqs,
        server_side = True
        )

        return client_ssl, addr



#定义一个基于 SSL 的 XML-RPC 服务器
# XML-RPC server with SSL
from xmlrpc.server import SimpleXMLRPCServer

class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass

#Here's the XML-RPC server from Recipe 11.6 modified only slightly to use SSL
import ssl
from xmlrpc.server import SimpleXMLRPCServer
from sslmixin import SSLMixin

class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


class KeyValueServer(object):
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']
    def __init__(self, *args, **kwargs):
        self.data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))


    def get(self, name):
        return self._data[name]


    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


if __name__ == '__main__':
    KEYFILE='server_key.pem' # Private key of the server
    CERTFILE='server_cert.pem' # Server certificate
    kvserv = KeyValueServer(('', 15000),
                            keyfile=KEYFILE,
                            certfile=CERTFILE
                            )
    kvserv.serve_forever()

