#!/usr/bin/env python
# -*- coding=utf-8 -*-

#select服务器, 包含writeList

import socket
import Queue
from select import select

SERVER_IP = ("", 9999)

#保存客户端发送过来的消息, 将消息放入队列中
message_queue = {}
input_list = []
output_list = []

if __name__ == "__main__":
    server = socket.socket()
    server.bind(SERVER_IP)
    server.listen(5)
    #设置为非阻塞
    server.setblocking(False)

    #初始化将服务端加入监听列表
    input_list.append(server)

    while True:
        #开始select监听, 对input_list中的服务端server进行监听
        stdinput, stdoutput, stderr = select(input_list, output_list, input_list)

        #循环判断是否有客户端链接进来, 当有客户端链接进来时select将触发
        for obj inn stdinput:
            #判断当前触发的是不是服务端对象, 当触发的是服务端对象时, 说明有新的客户端链接进来了
            if obj == server:
                #接收客户端的链接, 获取客户端对象和客户端信息地址
                conn, addr = server.accept()
                print("Client %s connected!"%str(addr))
                #将客户端对象也加入到监听列表中, 当客户端发送消息时select将触发
                input_list.append(conn)
                #为连接的客户端单独创建一个消息队列, 用来保存客户端发送的消息
                message_queue[conn] = Queue.Queue()

            else:
                #由于客户端连接进来时服务端接收客户端连接请求,将客户端加入到了监听列表中(input_list)中, 客户端发送消息将触发
                #所以判断是否是客户端对象触发
                try:
                    recv_data = obj.recv(1024)
                    #客户端未断开
                    if recv_data:
                        print("received %s from client %s"%(recv_data, str(addr)))
                        #将收到的消息放入到客户端的消息队列中
                        message_queue[obj].put(recv_data)


                        #将回复操作放到output列表中, 让select监听
                        if obj not in output_list:
                            output_list.append(obj)

                except ConnectionReseError:
                    #客户端断开连接, 将客户端的监听从inout列表中移除
                    input_list.remove(obj)
                    #移除客户端对象的消息列表
                    del message_queue[obj]
                    print("\n[input] Client %s disconnected"%str(addr))

            #如果现在没有客户端请求, 也没有客户端发送消息时, 开始对发送消息的列表进行处理,是否需要发送消息
            for sendobj in output_list:
                try:
                    #如果消息列队中有消息, 从消息队列中获取要发送的消息
                    if not message_queue[sendobj].empty():
                        #从该客户端对象的的消息队列中获取要发送的消息
                        send_data = message_queue[sendobj].get()
                        sendobj.send(send_data)
                    else:
                        #将监听移除等待下一次客户端发送消息
                        output_list.remove(sendobj)

                except ConnectionReseError:
                    #客户端连接断开了
                    del message_queue[sendobj]
                    output_list.remove(sendobj)
                    print("\n[output] Client %s disconnected"%str(addr))
