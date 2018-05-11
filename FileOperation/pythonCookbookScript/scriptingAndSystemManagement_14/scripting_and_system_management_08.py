#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 03:15:52 PM CST
# File Name: scripting_and_system_management_08.py
# Description: 给函数库增加日志功能, 但是又不能影响到那些不使用日志功能的程序
"""

#对于想要执行日志操作的函数库而已，应该创建一个专属的 logger 对象，并且初始化配置

#somelib.py

import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

#Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')


