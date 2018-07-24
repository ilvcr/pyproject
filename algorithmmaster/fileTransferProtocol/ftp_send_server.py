#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: ftp_send_server.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月24日 星期二 22时33分28秒
# Description: 
'''
    File transfer protocol used to send and receive files using FTP server.
    Use credentials to provide access to the FTP client
    
    Note: Do not use root username & password for security reasons
    Create a seperate user and provide access to a home directory of the user
    Use login id and password of the user created 
    cwd here stands for current working directory
'''
#************************************************************************#

from ftplib import FTP
ftp = FTP('xxx.xxx.x.x')  # Enter the ip address or the domain name here
ftp.login(user='username', passwd='password')
ftp.cwd('/Enter the directory here/')

"""
    The file which will be received via the FTP server
    Enter the location of the file where the file is received
"""

def ReceiveFile():
    FileName = 'example.txt'   """ Enter the location of the file """
    LocalFile = open(FileName, 'wb')
    ftp.retrbinary('RETR ' + FileName, LocalFile.write, 1024)
    ftp.quit()
    LocalFile.close()


"""
    The file which will be sent via the FTP server
    The file send will be send to the current working directory
"""
def SendFile():
    FileName = 'example.txt'   """ Enter the name of the file """
    ftp.storbinary('STOR ' + FileName, open(FileName, 'rb'))
    ftp.quit()



