#!/usr/bin/env python
# -*- coding=utf-8 -*-

#客户端

from socket import *
import random
import time

serverlp = raw_input("请输入服务器的ip:")
connNum = raw_input("请输入要连接服务器的次数(例如1000):")
g_socketList = []
for i in range(int(connNum)):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((serverlp, 7788))
    g_socketList.append(s)
    print(i)


while True:
    for s in g_socketList:
        s.send(str(random.randint(0, 100)))


    #用来测试
    #time.sleep(1)
