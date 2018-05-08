#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 08 May 2018 02:02:24 PM CST
# File Name: network_and_web_29.py
# Description:  一个简单的服务器演示如何使用线程池来实现耗时的计算
"""

# A really bad Fibonacci implementation
def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

class UDPFibServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(128)
        n = int(msg)
        pool.run(fib, (n, ), callback=lambda r:self.respond(r, addr))

    def respond(self, result, addr):
        self.sock.sendto(str(result).encode('ascii'), addr)


if __name__ == '__main__':
    pool = ThreadPoolHandler(16)
    handlers = [pool, UDPFibServer(('', 6000))]
    event_loop(handlers)


#运行服务器然后用 Python 程序来测试
from socket import *
sock = socket(AF_INET, AOCK_DGRAM)
for x in range(40):
    sock.sendto(str(x).encode('ascii'), ('locathost', 16000))
    resp = sock.recvfrom(8192)
    print(reso[0])
