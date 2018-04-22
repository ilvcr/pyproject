#!/usr/bin/env python
# -*- coding=utf-8 -*-

from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)#SOCK_STREAM是基于TCP的，数据传输比较有保障。SOCK_DGRAM是基于UDP的，专门用于局域网，基于广播

serverSocket.bind("", 8899) #绑定Ip和Port

serverSocket.listen(5)

print("------1------")
clientSocket, clientInfo = serverSocket.sccept()

print("------2------")
#clientSocket  表示这个新的客户端
#clientInfo     表示这个新的客户端的Ip和Port


recvData = clientSocket.recv(1024)

print("------3------")
print("%s:%s"%(str(clientInfo), recvData))

clientSocket.close()
serverSocket.close()
