#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: ftp_client_server.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月24日 星期二 22时23分34秒
# Description: 
#************************************************************************#

#server
import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = 'mytext.txt'
    f = open(filename, 'rb')
    in_data = f.read(1024)
    while(in_data):
        conn.send(in_data)
        print('Sent ', repr(in_data))
        in_data = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
        conn.close()


#client side server

import socket      # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data={}'.format(data))
        if not data:
            break
        #write data to a file
        f.write(data)

f.close()
print('successful get the file')
s.close()
print('connection closed')


