#!/usr/bin/env python
# -*- coding=utf-8 -*-

from socket import *

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    udpSocket.bind(("", 6789))#6789为端口号w为任意值

    while True:
        recvImfor = udpSocket.recvfrom(1024)
        print("[%s]:%s"%(str(recvImfor[1]), recvImfor[0].decode("gb2312")))


if __name__ == "__main__":
    main()
