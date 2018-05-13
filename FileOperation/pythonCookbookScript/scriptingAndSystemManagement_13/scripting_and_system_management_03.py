#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 02:44:21 PM CST
# File Name: scripting_and_system_management_03.py
# Description:  运行时弹出密码输入提示

                写了个脚本，运行时需要一个密码。此脚本是交互式的，
                因此不能将密码在脚本中硬编码，
                而是需要弹出一个密码输入提示，让用户自己输入。
"""


#Python 的 getpass 模块弹出密码输入提示，并且不会在用户终端回显密码

import getpass

user = getpass.getuser()
#user = input('Enter your username: ')
#显示的弹出用户名输入提示，使用内置的 input 函数

passwd = getpass.getpass()


if svc_login(user, passwd):   #You must write svc_login
    print('Yay!')
else:
    print('Boo!')

'''
svc login() 是要实现的处理密码的函数，具体的处理过程自己决定。
'''
