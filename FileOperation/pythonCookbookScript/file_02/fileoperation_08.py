#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Yoghourt.Lee->lvcr
# Created Time : Tue 17 Apr 2018 08:05:53 PM CST
# File Name: fileoperation_08.py
# Description:  代码功能：
                        safe_float()来处理信用卡交易文件, 将其作为字符串读入.
                        并用一个日志文件跟踪处理进程
"""

def safe_float(obj):
    '''safe version of float()'''
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval

def main():
    '''handle all the data processing'''
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError, e:
        log.write('no txns this month\n')
        log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')
        else:
            log.write('ignored: %s' %result)
    print('$%.2f(new balance)'%(tatal))
    log.close()

if __name__ == '__main__':
    main()

