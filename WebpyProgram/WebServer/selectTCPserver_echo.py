#!/usr/bin/env python
# -*- coding=utf-8 -*-

#select版--TCP服务器

#select回显服务器

#使用python的select模块很容易写出一个echo(回显)服务器:

import select
import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind("", 7788)
server.listen(5)

imputs = [server, sys.stdin]

running = True

while True:

    #调用select函数, 阻塞等待
    readable, writeable, exceptional = select.select(inputs, [], [])

    #数据抵达, 循环
    for sock in readable:

        #监听到所有的链接
        if sock == server:
            conn, addr = server.accept()
            #select监听的socket
            inputs.append(conn)


        #监听到键盘有输入
        elif sock == sys.stdin.readline()
        running = False
        break

        #有数据到达
        else:
            #读取客户端连接发送的数据
            data = socket.recv(1024)
            if data:
                sock.send(data)
            else:
                #移除select监听的socket
                inputs.remove(sock)
                sock.close()

    #如果检测到用户输入敲击键盘, 就退出
    if not running:
        break

server.close()
