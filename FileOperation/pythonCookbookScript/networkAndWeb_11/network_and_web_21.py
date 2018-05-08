#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Sun 06 May 2018 04:38:41 PM CST
# File Name: network_and_web_21.py
# Description:  建立一个安全的 XML-RPC 连接来确认服务器证书
"""

from xmlrpc.client import SafeTransport, ServerProxy
import ssl

class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if cert:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRES


    def make_connection(self, host):
        # Items in the passed dictionary are passed as keyword
        # arguments to the http.client.HTTPSConnection() constructor.
        # The context argument allows an ssl.SSLContext instance to
        # be passed with information about the SSL configuration
        s = super().make_connection((host, {'context': self._ssl_context}))

        return s

#Create the client proxy
s = ServerProxy('https://localhost:15000', transport=VerifyCertSafeTransport('server_cert.pem'), allow_none=True)


#服务器将证书发送给客户端，客户端来确认它的合法性, 服务器启动代码如下
if __name__ == '__main__':

    KEYFILE='server_key.pem' # Private key of the server
    CERTFILE='server_cert.pem' # Server certificate
    CA_CERTS='client_cert.pem' # Certificates of accepted clients
    kvserv = KeyValueServer(('', 15000),
                            keyfile=KEYFILE,
                            certfile=CERTFILE,
                            ca_certs=CA_CERTS,
                            cert_reqs=ssl.CERT_REQUIRED,
                            )

    kvserv.serve_forever()


#修改 ServerProxy 的初始化代码让 XML-RPC 客户端发送证书
# Create the client proxy
s = ServerProxy('https://localhost:15000',
                transport=VerifyCertSafeTransport(  'server_cert.pem',
                                                    'client_cert.pem',
                                                    'client_key.pem'),
                                                    allow_none=True)
