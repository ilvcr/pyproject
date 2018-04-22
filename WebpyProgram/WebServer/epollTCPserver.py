#!/usr/bin/env python
# -*- coding=utf-8 -*-

#epoll版--TCP服务器

import socket
import select


#创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#设置可以重复使用绑定的信息
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#绑定本地信息
s.bind(("", 7788))

#变为被动
s.listen(10)

#创建一个epoll对象
epoll = select.epoll()

#测试, 用来打印套接字对应文件描述符
#print(s.fileno())
#print(select.EPOLLIN|select.EPOLLET)

#注册事件到epoll中
#epoll.register(fd[, eventmask])
#注意, 如果fd已经注册过, 则会发生异常
#将创建的套接字添加到epoll的事件监听中
epoll.register(s.fileno(), select.EPOLLIN|select.EPOLLET)

connections = {}
addresses = {}

#循环等待客户端的到来或者对方发送数据
while True:

    #epoll进行fd扫描的地方 -- 未指定超过时间则视为阻塞等待
    epoll_list = epoll.poll()

    #对事件进行判断
    for fd, events in epoll_list:

        #print fd
        #print events

        #如果是socket创建的套接字被激活
        if fd == s.fileno():
            conn, addr = s.accept()

            print("有新的客户端到来%s"%str(addr))

            #将conn和addr信息分别保存起来
            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr

            #向epoll中注册链接socket的可读事件
            epoll.register(conn.fileno(), select.EPOLLIN|select.EPOLLET)

        elif events == select.EPOLLIN:
            #从激活fd上接收
            recvData = connections[fd].recv(1024)

            if len(recvData) > 0:
                print("recv:%s"%recvData)
            else:
                #从epoll中移除该链接fd
                epoll.unregister(fd)

                #server侧主动关闭该链接fd
                connections[fd].close()

                print("%s---offline----"%str(addresses[fd]))


'''
SUMMARY:

    1-> EPOLLIN （可读）
    2-> EPOLLOUT （可写）
    3-> EPOLLET （ET模式）
epoll对文件描述符的操作有两种模式：LT（level trigger）和ET（edgetrigger）。LT模式是默认模式，LT模式与ET模式的区别如下：

        1-> LT模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。下次调用epoll时，会再次响应应用程序并通知此事件。

        2-> ET模式：当epoll检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。如果不处理，下次调用epoll时，不会再次响应应用程序并通知此事件。
'''
