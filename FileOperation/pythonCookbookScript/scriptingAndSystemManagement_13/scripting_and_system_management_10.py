#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Fri 11 May 2018 03:30:48 PM CST
# File Name: scripting_and_system_management_10.py
# Description:  在 Unix 系统上面运行的程序设置内存或 CPU 的使用限制
"""


#resource 模块能同时执行限制内存和 CPU 的使用量这两个任务

import signal
import resource
import os


def time_exceeded(signo, frame):
    print("Time's up!")
    raise SystemExit(1)


def set_max_runtime(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)  #程序运行时，SIGXCPU信号在时间过期时被生成，然后执行清理并退出。

def limit_memory(maxsize):
    '''
    限制内存使用，设置可使用的总内存值
    '''
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass

