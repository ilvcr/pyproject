#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 03:07:47 PM CST
# File Name: scripting_and_system_management_07.py
# Description:  给简单脚本增加日志功能
"""

'''
在脚本和程序中将诊断信息写入日志文件

打印日志最简单方式是使用 logging 模块
'''

import logging

def main():
    #configure the logging system
    logging.basicConfig(
                        filename = 'app.log',
                        level=logging.ERROR
                        )

    #Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'


    #Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info("opening file %r, mode=%r", filename, mode)
    logging.debug('Get here')


if __name__ == '__main__':
    main()
